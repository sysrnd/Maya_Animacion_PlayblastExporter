import maya.cmds as cmds
import maya.mel as mel
import os

class playblastExport(object):
	def __init__(self):
		self.file = cmds.file(q=True, sn=True)
		self.alignments = {'bottom_right':(0.45,-0.20,-1.0), 'upper_right':(0.45,0.20,-1.0), 'center_right':(0.23,0,-1.0),
		'bottom_left':(0.3,-0.3,-1.0), 'upper_left':(0.3,-0.2,-1.0), 'center_left':(0.3,-0.3,-1.0),
		'bottom_center':(0.3,-0.3,-1.0), 'upper_center':(0.3,-0.3,-1.0), 'center':(0, 0, -1.0)}
	def main(self, txt, path):
		camera = self.active_camera()
		
		if camera != None:
			self.filePath = self.filePath_()
			shader = self.create_shader()
			text = self.text(txt)
			self.assign_shader(shader[0], shader[1], text)
			self.constraint(text, camera)
			self.offset(text, 'bottom_right')
			time = self.headsUpDisplay()
			self.showHideViewport(False)
			self.showHideSafeAction(camera)
			self.playblast(path)
			self.showHideViewport(True)
			self.delete(text, camera)
			#print 'playblast exportado en ' + path,
		else:
			cmds.warning('Must select a viewport')
	def fileName(self):
		fileName = self.file.split('/')[-1].strip('.ma')
		return fileName
	def filePath_(self):
		if self.file.endswith('.ma'):
			filePath = str(self.file.strip('.ma'))
		else:
			filePath = str(self.file.strip('.mb'))
		return filePath
	def text(self, txt):
		label_curves_grp = cmds.textCurves(constructionHistory=0, text=txt, font='Courier')[0]
		label_curves_ch = cmds.listRelatives(label_curves_grp, children=True)
		label_surfaces = []
		#label_surfaces_grp = cmds.group(em=True, n=txt + '_grp')
		for x in label_curves_ch:
			srf = cmds.planarSrf(x, tolerance=0.01, constructionHistory=False, object=True, polygon=True)[0]
			label_surfaces.append(srf)

		cmds.delete(label_curves_grp)
		label_surfaces_grp_offset = cmds.group(label_surfaces, n= txt + '_grp_offset')
		label_surfaces_grp = cmds.group(label_surfaces_grp_offset, n= txt + '_grp')
		return label_surfaces_grp_offset
	def create_shader(self):
		shader=cmds.shadingNode("surfaceShader",asShader=True)
		shading_grp= cmds.sets(renderable=True,noSurfaceShader=True,empty=True)
		cmds.setAttr(shader + '.outColor', 1, 1, 1,type='double3')
		return shader, shading_grp
	def assign_shader(self, shader, shading_grp, geo):
		cmds.connectAttr('%s.outColor' %shader ,'%s.surfaceShader' %shading_grp)
		cmds.select(cl=True)
		cmds.select(geo, hi=True)
		cmds.hyperShade(assign=shader)
		cmds.select(cl=True)
	def constraint(self, geo, camera):
		geo = cmds.listRelatives(geo, parent=True)
		cmds.parentConstraint(camera, geo, mo=False)
	def offset(self, geo, al):
		axis = ['X','Y','Z']
		geoParent = cmds.listRelatives(geo, parent=True)[0]
		for ax in range(0, 3):
			cmds.setAttr(geo + '.scale' + axis[ax], 0.005)
			cmds.setAttr(geo + '.translate' + axis[ax], self.alignments[al][ax])
	def active_camera(self):
		self.panel = cmds.getPanel(withFocus=True)
		if (cmds.getPanel(typeOf=self.panel) == "modelPanel"):
			camera = cmds.modelEditor(self.panel, q=True, camera=True)
		else:
			return None
		return camera
	def showHideViewport(self, bool):
		
		
		if bool == False:
			self.activeViewports = []
			flags = ['lights', 'cameras', 'nurbsCurves', 'joints', 'locators']
			
			for flag in flags:
				flagBool = {flag: bool}
				flagVis = {flag: True}
				active = cmds.modelEditor(self.panel, q=True, **flagVis)
				if active == True:
					active = cmds.modelEditor(self.panel, e=True, **flagBool)
					self.activeViewports.append(flag)
		else:
			for active in self.activeViewports:
				flagBool = {active: bool}
				active = cmds.modelEditor(self.panel, e=True, **flagBool)
	def showHideSafeAction(self, camera):

		cmds.camera(camera, e=True, dgm=False, dfg=False, dfc=False, dr=False,ff='horizontal', overscan=1)
	def headsUpDisplay(self):
		
		allHuds = cmds.headsUpDisplay(lh=True)
		activeHuds = []
		if allHuds != None:
			for hud in allHuds:
				active = cmds.headsUpDisplay(hud, q=True, vis=True)
				if active == 1:
					cmds.headsUpDisplay(hud, e=True, vis=False)
					activeHuds.append(hud)
		try:
			time = cmds.headsUpDisplay('time', l='Frame: ', pre='currentFrame', s=5, b=2, lfs='large',dfs='large')
			return time
		except:
			pass
	def playblast(self, path):
		
		start = int(cmds.playbackOptions(q=True, min=True))
		end = int(cmds.playbackOptions(q=True, max=True))
		audio = cmds.ls(et='audio')
		sceneName = self.fileName()
		if len(audio) > 0:
			cmds.playblast(st=start, et=end, filename=path + '/' + sceneName + '.mov', clearCache=True, fo=True,fmt='qt', useTraxSounds=True, s=audio[0],compression='H.264', p=100, widthHeight = (1920, 1080))
		else:
			cmds.playblast(st=start, et=end, filename=path + '/' + sceneName + '.mov', clearCache=True, fo=True,fmt='qt', compression='H.264', p=100, widthHeight = (1920, 1080))
	
		
	def delete(self, txt, camera):
		cmds.delete(cmds.listRelatives(txt, parent=True)[0])
		cmds.headsUpDisplay('time', rem=True)
		cmds.camera(camera, e=True, overscan=1)
	def getDocsPath(self):
		docsPath = os.getenv("HOME")
		return docsPath
	def path(self):
		cagon = cmds.fileDialog2(fm=3, dialogStyle=2, cc='Cancel')
		if cagon:
			return cagon[0]
	def warnings(self, artist):
		cmds.warning(artist + ': Debes seleccionar una ruta ubicada en Z:/ o en //Master ')
#play = playblastExport()
#play.main('Sasa Rodriguez')
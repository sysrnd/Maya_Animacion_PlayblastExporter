'''
from slackclient import SlackClient
slack_client = SlackClient(os.environ.get('SLACK_TOKEN', None))
slack_client.api_call("chat.postMessage", channel="rnd", text='test')
'''
class Slack(object):
	def MessageSlack(self, Message, channel = None):
		import sys
		sys.path.append("Z:/RnD/Python/Python27/Lib/site-packages/requests")
		sys.path.append("Z:/RnD/Python/Python27/Lib/site-packages")
		import json
		import requests
		PlayblastWH = "https://hooks.slack.com/services/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"
		webhook_url = "https://hooks.slack.com/services/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"
		channel_ = "mexicartoons"
		teamName = "mkfanimation"
		token_ = "4Yy9aL8SDNduuhME0qFRol7N"

		if channel != None:
			channel_ = channel
		
		slack_data = {
		'channel':channel_,
		'text': Message}
		
		response = requests.post(
		    webhook_url, data=json.dumps(slack_data),
		    headers={'Content-Type': 'application/json'}
		)
		if response.status_code != 200:
		    raise ValueError(
		        'Request to slack returned an error %s, the response is:\n%s'
		        % (response.status_code, response.text)
		    )
#slack = Slack()
#slack.MessageSlack("Se ha salvado el playblast", channel = "rnd")
#region[event]
import requests
import json
import sys
import os
from dotenv import load_dotenv
#endregion
#region[var]
load_dotenv()
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
SLACK_APP_TOKEN = os.environ['SLACK_APP_TOKEN']
slack_channel = "C03M95BLRFX" #Conversation ID for #Slack channel
slack_text = sys.argv[1]
#slack_text = "Testing"
#endregion
#region[function]
def post_message_to_slack(text, blocks = None):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': SLACK_BOT_TOKEN,
        'channel': slack_channel,
        'text': text,
        'icon_emoji': ':cow:',
        'username': 'Random Cow',
        'blocks': json.dumps(blocks) if blocks else None
    }).json()
#endregion
#region[main]
post_message_to_slack(slack_text)
#endregion
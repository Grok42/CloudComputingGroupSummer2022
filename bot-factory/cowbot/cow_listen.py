from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from dotenv import load_dotenv
import re
import subprocess

load_dotenv()
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
SLACK_APP_TOKEN = os.environ['SLACK_APP_TOKEN']


def call_cowsay(text):
    py_cow = "~/Coding/Cloud/pyCowSlack/cowsay.py"
    cmd = ["Python3", py_cow, text] 
    ec = subprocess.call(cmd)

app = App(token=SLACK_BOT_TOKEN)

#@app.event("app_mention")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
#def mention_handler(body, say):
#        say('Hello World!')
#        say('You said: ' + body["event"]["text"])
        
@app.event("message")
def handle_rcvg_codes_events(body,say):
    channel = body["event"]["channel"]
    if channel == "C03M95BLRFX":  #Conversation ID for #Slack channel
        msg = body["event"]["text"]
        regex = '^(Cowsay|COWSAY|cowsay)\s'
        if re.match(regex,msg):
            reply = re.sub(regex,'',msg)
            call_cowsay(reply)
        
if __name__ == "__main__":
        handler = SocketModeHandler(app, SLACK_APP_TOKEN)
        handler.start()
from slack_sdk import WebClient
from bs4 import BeautifulSoup 
import slack_sdk
import os
from pathlib import Path
from dotenv import load_dotenv

from fpdf import FPDF
import requests 

from aika import *
from ruokapaikat import *
from blockkit import Button, Context, Divider, Message, Section

import json

from slack_sdk.webhook import WebhookClient

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


env_path = Path('.') /'.env'
load_dotenv(dotenv_path=env_path)


client = WebClient(token=os.environ['SLACK_TOKEN'])

app = App(token=os.environ["SLACK_TOKEN"])

with open('buttons.json') as user_file:
  file_contents = user_file.read()

parsed_json = json.loads(file_contents)


    




@app.action("button_click")
def action_button_click(body, ack, say):
    # Acknowledge the action
    ack()
    say(f"<@{body['user']['id']}> äänesti ravintolaa Wolkoff")

if __name__ == "__main__":
    client.chat_postMessage(channel='#lunch-bot', blocks=json.dumps(parsed_json))
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
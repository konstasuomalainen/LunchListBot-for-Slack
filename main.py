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

import schedule
import time

env_path = Path('.') /'.env'
load_dotenv(dotenv_path=env_path)


client = WebClient(token=os.environ['SLACK_TOKEN'])

app = App(token=os.environ["SLACK_TOKEN"])

with open('buttons.json') as user_file:
  file_contents = user_file.read()

parsed_json = json.loads(file_contents)

timestamp1 = ""
user_id = ""
äänestäjät = []
äänestäjät1 = []
äänestäjät2 = []
äänestäjät3 = []
size1= []
size2= []
size3= []
res = []
ravintola1 = ['Cafe Hullu','Pancho Villa','Wolkoff']

response = app.client.conversations_list()
channel_name = 'lunch-bot'  # Replace with your channel name
channel_id = None
for channel in response['channels']:
    if channel['name'] == channel_name:
        channel_id = channel['id']
        break
if channel_id:
    print(f"Channel ID for '{channel_name}': {channel_id}")
else:
    print(f"Channel '{channel_name}' not found.")


datas1 = find_ruoka1()
datas2 = find_ruoka2()
datas3= find_ruoka3()


    
def ruokanaTänään():

    
    for data in datas1:
        data = data.text
        #JOS TÄMÄ PÄIVÄMÄÄRÄ LÖYTYY RUOKALISTALTA, ruokalista tulostuu slackkiin
        if aika() in data:
        
            kaava2 = data
            
            kaava2 = data.replace('€', ' euro ')
            res = [ravintola1[0]]
            result = ''.join(res)
            print(kaava2)
            client.chat_postMessage(channel='#lunch-bot', text="",
            blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f'{result}:\n{kaava2}!'},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Vote"},
                    "action_id": "button_click1"
                },
                
            }
            ])
            
        
        
        else:
            #VIIKONLOPPU TAI EI RUOKAILUA
            print("ei ruokailua")

    for data in datas2:
        data = data.text
        #JOS TÄMÄ PÄIVÄMÄÄRÄ LÖYTYY RUOKALISTALTA, ruokalista tulostuu slackkiin
        if aika() in data:
        
            kaava2 = data
            
            kaava2 = data.replace('€', ' euro ')
            res = [ravintola1[1]]
            result = ''.join(res)
            print(kaava2)
            client.chat_postMessage(channel='#lunch-bot', text="",
            blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f'{result}:\n{kaava2}!'},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Vote"},
                    "action_id": "button_click2"
                },
                
            }
            ])
            
        
        
        else:
            #VIIKONLOPPU TAI EI RUOKAILUA
            print("ei ruokailua")
    for data in datas3:
        data = data.text
        #JOS TÄMÄ PÄIVÄMÄÄRÄ LÖYTYY RUOKALISTALTA, ruokalista tulostuu slackkiin
        if aika() in data:
        
            kaava2 = data
            
            kaava2 = data.replace('€', ' euro ')
            res = [ravintola1[2]]
            result = ''.join(res)
            print(kaava2)
            client.chat_postMessage(channel='#lunch-bot', text="",
            blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f'{result}:\n{kaava2}!'},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Vote"},
                    "action_id": "button_click3"
                },
                
            }
            ])
            
        
        else:
            #VIIKONLOPPU TAI EI RUOKAILUA
            print("ei ruokailua")
    global timestamp1
    vastaus1=client.chat_postMessage(channel='#lunch-bot', text="Kukaan ei ole äänestänyt vielä")
    timestamp1 = vastaus1['ts']
    








   
def äänestys():
    
    global timestamp1
    if timestamp1:
            
            timestamp2 = timestamp1
            res1 = [ravintola1[0]]
            result1 = ''.join(res1)
            res2 = [ravintola1[1]]
            result2 = ''.join(res2)
            res3 = [ravintola1[2]]
            result3 = ''.join(res3)
            if timestamp1:
                global size1
                global size2
                global size3
                #Update the previous message with the current vote count
                client.chat_update(
                channel=channel_id,
                ts=f"{timestamp2}",
                text=f"({size1}) on äänestänyt ravintolaa {result1}, ({size2}) on äänestänyt ravintolaa {result2}, ({size3}) on äänestänyt ravintolaa {result3}"
                )
                
                
            else:
                # Post a new message and store the timestamp
                vastaus = client.chat_postMessage(
                channel='#lunch-bot',
                text=f"{size1} on äänestänyt ravintolaa {result1}, {size2} on äänestänyt ravintolaa {result2}, {size3} on äänestänyt ravintolaa {result3}",
                timestamp1 = vastaus['ts'])


@app.action("button_click1")
def action_button_click3(body, ack):
    
    ack()
    user_id = body['user']['id']
    if user_id not in äänestäjät:
        äänestäjät.append(user_id)

    # Check if the user has already voted
    if user_id in äänestäjät:
        äänestäjät1.append(user_id)
        global size1
        äänestäjät11 = list(set(äänestäjät1))
        size1 = len(äänestäjät11)
        äänestys()
@app.action("button_click2")
def action_button_click3(body, ack):
    
    ack()
    user_id = body['user']['id']
    if user_id not in äänestäjät:
        äänestäjät.append(user_id)

    # Check if the user has already voted
    if user_id in äänestäjät:
        äänestäjät2.append(user_id)
        global size2
        äänestäjät22 = list(set(äänestäjät2))
        size2 = len(äänestäjät22)
        äänestys()
@app.action("button_click3")
def action_button_click3(body, ack):
    
    ack()
    user_id = body['user']['id']
    if user_id not in äänestäjät:
        äänestäjät.append(user_id)

    # Check if the user has already voted
    if user_id in äänestäjät:
        äänestäjät3.append(user_id)
        global size3
        äänestäjät33 = list(set(äänestäjät3))
        size3 = len(äänestäjät33)
        äänestys()

        
        
     
                

        
   
    
    
    




if __name__ == "__main__":
    ruokanaTänään()
    #client.chat_postMessage(channel='#lunch-bot', blocks=json.dumps(parsed_json))
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

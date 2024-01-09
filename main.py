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


    
äänestäjät = []
size1= []
res = []
ravintola1 = ['Cafe Hullu','Pancho Villa','Wolkoff']



datas1 = find_ruoka1()
datas2 = find_ruoka2()
datas3= find_ruoka3()


    

    
    
def ruokana1():
    
    for data in datas1:
        data = data.text
        #JOS TÄMÄ PÄIVÄMÄÄRÄ LÖYTYY RUOKALISTALTA, ruokalista tulostuu slackkiin
        if aika() in data:
        
            kaava2 = data
            
            kaava2 = data.replace('€', ' euro ')
            res = [ravintola1[0]]
            print(kaava2)
            client.chat_postMessage(channel='#lunch-bot', text="",
            blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f'{res}:\n{kaava2}!'},
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



@app.action("button_click1")
def action_button_click1(body, ack, say):
    # Acknowledge the action
    ack()
    #say(f"<@{body['user']['id']}> äänesti ravintolaa {ravintola}")
    new_äänestäjä = f"<@{body['user']['id']}>"
    äänestäjät.append(new_äänestäjä)
    äänestäjät1 = list(set(äänestäjät))
    size1 = len(äänestäjät1)
    res = [ravintola1[0]]
    say(f"({size1}) äänesti ravintolaa {res}")
  
def ruokana2():
    
    for data in datas2:
        data = data.text
        #JOS TÄMÄ PÄIVÄMÄÄRÄ LÖYTYY RUOKALISTALTA, ruokalista tulostuu slackkiin
        if aika() in data:
        
            kaava2 = data
            
            kaava2 = data.replace('€', ' euro ')
            res = [ravintola1[1]]
            print(kaava2)
            client.chat_postMessage(channel='#lunch-bot', text="",
            blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f'{res}:\n{kaava2}!'},
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




@app.action("button_click2")
def action_button_click2(body, ack, say):
    # Acknowledge the action
    ack()
    #say(f"<@{body['user']['id']}> äänesti ravintolaa {ravintola}")
    new_äänestäjä = f"<@{body['user']['id']}>"
    äänestäjät.append(new_äänestäjä)
    äänestäjät1 = list(set(äänestäjät))
    size1 = len(äänestäjät1)
    res = [ravintola1[1]]
    
    say(f"({size1}) äänesti ravintolaa {res}")   


def ruokana3():
    
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




@app.action("button_click3")
def action_button_click3(body, ack, say):
    
    ack()
    #say(f"<@{body['user']['id']}> äänesti ravintolaa {ravintola}")
    new_äänestäjä = f"<@{body['user']['id']}>"
    äänestäjät.append(new_äänestäjä)
    äänestäjät1 = list(set(äänestäjät))
    size1 = len(äänestäjät1)
    res = [ravintola1[2]]
    #poistaa bracketit
    result = ''.join(res)
    if size1 > 0:
        while True:
            #30 min jälkeen äänestystulokset julkaistaan
            time_wait = 30
            time.sleep(time_wait * 60)
            print(f'Waiting {time_wait} minutes')
            say(f"({size1}) äänesti ravintolaa {result}")
            break
            
    
    
    
    




if __name__ == "__main__":
    ruokana1()
    ruokana2()
    ruokana3()
    #client.chat_postMessage(channel='#lunch-bot', blocks=json.dumps(parsed_json))
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

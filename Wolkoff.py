
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



with open('buttons.json') as user_file:
  file_contents = user_file.read()

parsed_json = json.loads(file_contents)


env_path = Path('.') /'.env'
load_dotenv(dotenv_path=env_path)


client = WebClient(token=os.environ['SLACK_TOKEN'])





datas = find_ruoka3()



 
for data in datas:
    data = data.text
    #JOS TÄMÄ PÄIVÄMÄÄRÄ LÖYTYY RUOKALISTALTA, ruokalista tulostuu slackkiin
    if aika() in data:
        
        kaava1 = data
        
        kaava1 = data.replace('€', ' euro')
        client.chat_postMessage(channel='#lunch-bot', text = (f'Wolkoff lounas:\n>{kaava1}\n>'))
        
        
        print(kaava1)
        
        
        break
    else:
        #VIIKONLOPPU TAI EI RUOKAILUA
        print("ei ruokailua")
        
        
        break
        
        










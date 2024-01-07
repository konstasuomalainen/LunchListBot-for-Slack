
from slack_sdk import WebClient
from bs4 import BeautifulSoup 

import os
from pathlib import Path
from dotenv import load_dotenv

from fpdf import FPDF

from aika import *

from ruokapaikat import *

env_path = Path('.') /'.env'
load_dotenv(dotenv_path=env_path)



client = WebClient(token=os.environ['SLACK_TOKEN'])



datas = find_ruoka1()


for data in datas:
    data = data.text
    #JOS TÄMÄ PÄIVÄMÄÄRÄ LÖYTYY RUOKALISTALTA, ruokalista tulostuu slackkiin
    if aika() in data:
        
        kaava3 = data
  
        print(kaava3)
        #client.chat_postMessage(channel='#lunch-bot', text = (f'Cafe Hullu Lounas:\n{kaava3}'))
        
        break
    else:
        #VIIKONLOPPU TAI EI RUOKAILUA
        print("ei ruokailua")
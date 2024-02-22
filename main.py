from slack_sdk import WebClient
from bs4 import BeautifulSoup 
import slack_sdk
import os
from pathlib import Path
from dotenv import load_dotenv
import requests
from aika import *
from ruokapaikat import *
from blockkit import Button, Context, Divider, Message, Section
from slack_sdk.webhook import WebhookClient
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import time

env_path = Path('.') /'.env'
load_dotenv(dotenv_path=env_path)


client = WebClient(token=os.environ['SLACK_TOKEN'])

app = App(token=os.environ["SLACK_TOKEN"])




user_id = ""

voter_ids1 = []
voter_ids2 = []
voter_ids3 = []
voter_ids4 = []
voter_ids5 = []
voter_ids6 = []
voter_ids7 = []
voter_ids8 = []
voter_idsMuu = []
vote_count1= []
vote_count2= []
vote_count3= []
vote_count4= []
vote_count5= []
vote_count6= []
vote_count7= []
vote_count8= []
vote_countMuu= []


all_restaurants = ['Cafe Hullu','Pancho Villa','Wolkoff', 'Wilhelmiina','Elsi','Kehruuhuone','Vapari', 'Kitchen', 'Muu']

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


menu1 = find_ruoka1()
menu2 = find_ruoka2()
menu3 = find_ruoka3()
menu4 = find_ruoka4()
menu5 = find_ruoka5()
menu6 = find_ruoka6()
menu7 = find_ruoka7()
menu8 = find_ruoka8()



    
def ruokanaTänään():
    messages_sent = False

    # List of menus
    menus = [menu1, menu2, menu3, menu4, menu5, menu6, menu7, menu8]

    for menu in menus:
        for ruokana in menu:
            ruokana = ruokana.text

            # If today's date is found on the menu, the menu will be printed to Slack
            if aika() in ruokana:
                client.chat_postMessage(channel='#lunch-bot', text="",
                blocks=[
                {
			    "type": "header",
			    "text": {
				"type": "plain_text",
				"text": ":newspaper:  Päivän Lounaslista  :newspaper:"
			    },}])
                break
        break




    for ruokana in menu1:
        ruokana = ruokana.text
        #If today's date is found on the menu, the menu will be printed to Slack
        if aika() in ruokana:
            
            ruokana = ruokana.replace('€', ' euro ')
            
            res = [all_restaurants[0]]
            result = ''.join(res)
            print(ruokana)
            client.chat_postMessage(channel='#lunch-bot', text="",
            blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f'*{result}*:\n\n{ruokana}!'},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Vote"},
                    "action_id": "vote_click1"
                },
                
            }
            ])
            messages_sent = True
        
        
        else:
            #Weekend or no meals
            print("ei ruokailua")

    for ruokana in menu2:
        ruokana = ruokana.text
        #If today's date is found on the menu, the menu will be printed to Slack
        if aika() in ruokana:
            
            ruokana = ruokana.replace('€', ' euro ')
            
            
            res = [all_restaurants[1]]
            result = ''.join(res)
            print(ruokana)
            client.chat_postMessage(channel='#lunch-bot', text="",
            blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f'*{result}*:\n\n{ruokana}!'},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Vote"},
                    "action_id": "vote_click2"
                },
                
            }
            ])
            messages_sent = True
        
        
        else:
            #Weekend or no meals
            print("ei ruokailua")
    for ruokana in menu3:
        ruokana = ruokana.text
        #If today's date is found on the menu, the menu will be printed to Slack
        if aika() in ruokana:
            
            ruokana = ruokana.replace('€', ' euro ')
            ruokana = ruokana.replace('Perjantai 9.2.', '')
            res = [all_restaurants[2]]
            result = ''.join(res)
            print(ruokana)
            client.chat_postMessage(channel='#lunch-bot', text="",
            blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f'*{result}*:\n{ruokana}!'},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Vote"},
                    "action_id": "vote_click3"
                },
                
            }
            ])
            messages_sent = True
        
        else:
            #Weekend or no meals
            print("ei ruokailua")
    for ruokana in menu4:
        ruokana = ruokana.text
        #If today's date is found on the menu, the menu will be printed to Slack
        if aika() in ruokana:
            
            ruokana = ruokana.replace('€', ' euro ')
            ruokana = ruokana.replace('Perjantai 9.2.', '')
            res = [all_restaurants[3]]
            result = ''.join(res)
            print(ruokana)
            client.chat_postMessage(channel='#lunch-bot', text="",
            blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f'*{result}*:\n\n{ruokana}!'},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Vote"},
                    "action_id": "vote_click4"
                },
                
            }
            ])
            messages_sent = True
        
        else:
            #Weekend or no meals
            print("ei ruokailua")
    for ruokana in menu5:
        ruokana = ruokana.text
        #If today's date is found on the menu, the menu will be printed to Slack
        if aika() in ruokana:
            
            ruokana = ruokana.replace('€', ' euro ')
            ruokana = ruokana.replace('Perjantai 9.2.', '')
            res = [all_restaurants[4]]
            result = ''.join(res)
            print(ruokana)
            client.chat_postMessage(channel='#lunch-bot', text="",
            blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f'*{result}*:\n\n{ruokana}!'},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Vote"},
                    "action_id": "vote_click5"
                },
                
            }
            ])
            messages_sent = True
        
        else:
            #weekend or no meals
            print("ei ruokailua")
    for ruokana in menu6:
        ruokana = ruokana.text
        #If today's date is found on the menu, the menu will be printed to Slack
        if aika() in ruokana:
            
            ruokana = ruokana.replace('€', ' euro ')
            
            
            res = [all_restaurants[5]]
            result = ''.join(res)
            print(ruokana)
            client.chat_postMessage(channel='#lunch-bot', text="",
            blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f'*{result}*:\n\n{ruokana}!'},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Vote"},
                    "action_id": "vote_click6"
                },
                
            }
            ])
            messages_sent = True
        
        
        else:
            #Weekend or no meals
            print("ei ruokailua")      

    for ruokana in menu7:
        ruokana = ruokana.text
        #If today's date is found on the menu, the menu will be printed to Slack
        if aika() in ruokana:
            
            ruokana = ruokana.replace('€', ' euro ')
            
            
            res = [all_restaurants[6]]
            result = ''.join(res)
            print(ruokana)
            client.chat_postMessage(channel='#lunch-bot', text="",
            blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f'*{result}*:\n\n{ruokana}!'},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Vote"},
                    "action_id": "vote_click7"
                },
                
            }
            ])
            messages_sent = True
        
        
        else:
            #Weekend or no meals
            print("ei ruokailua")  

    for ruokana in menu8:
        ruokana = ruokana.text
        #If today's date is found on the menu, the menu will be printed to Slack
        if aika() in ruokana:
            
            ruokana = ruokana.replace('€', ' euro ')
            
            
            res = [all_restaurants[7]]
            result = ''.join(res)
            print(ruokana)
            client.chat_postMessage(channel='#lunch-bot', text="",
            blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f'*{result}*:\n\n{ruokana}!'},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Vote"},
                    "action_id": "vote_click8"
                },
                
            }
            ])
            messages_sent = True
        
        
        else:
            #Weekend or no meals
            print("ei ruokailua")   
    if messages_sent == True:
        client.chat_postMessage(channel='#lunch-bot', text="",
            blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f'*Muu ravintola*'},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Vote"},
                    "action_id": "vote_click9"
                },
                
            }
            ])
            
    if messages_sent == True:
        global VoteMessageTs
        vastaus1=client.chat_postMessage(channel='#lunch-bot', text="*Kukaan ei ole äänestänyt vielä*")
        VoteMessageTs = vastaus1['ts']
    








   
def äänestys():
    global vote_count1
    global vote_count2
    global vote_count3
    global vote_count4
    global vote_count5
    global vote_count6
    global vote_count7
    global vote_count8
    global vote_countMuu
    global VoteMessageTs
    vote_count1 = len(voter_ids1)
    vote_count2 = len(voter_ids2)
    vote_count3 = len(voter_ids3)
    vote_count4 = len(voter_ids4)
    vote_count5 = len(voter_ids5)
    vote_count6 = len(voter_ids6)
    vote_count7 = len(voter_ids7)
    vote_count8 = len(voter_ids8)
    vote_countMuu = len(voter_idsMuu)

    if VoteMessageTs:
            
            
            res1 = [all_restaurants[0]]
            res1 = ''.join(res1)
            res2 = [all_restaurants[1]]
            res2 = ''.join(res2)
            res3 = [all_restaurants[2]]
            res3 = ''.join(res3)
            res4 = [all_restaurants[3]]
            res4 = ''.join(res4)
            res5 = [all_restaurants[4]]
            res5 = ''.join(res5)
            res6 = [all_restaurants[5]]
            res6 = ''.join(res6)
            res7 = [all_restaurants[6]]
            res7 = ''.join(res7)
            res8 = [all_restaurants[7]]
            res8 = ''.join(res8)
            resMuu = [all_restaurants[8]]
            resMuu = ''.join(resMuu)
            
 

            # Create a list of tuples containing vote counts, restaurant names, and indices
            restaurant_data = [
            (vote_count1, res1, 1),
            (vote_count2, res2, 2),
            (vote_count3, res3, 3),
            (vote_count4, res4, 4),
            (vote_count5, res5, 5),
            (vote_count6, res6, 6),
            (vote_count7, res7, 7),
            (vote_count8, res6, 8),
            (vote_countMuu, resMuu, 9)
            ]

            # Sort the list based on vote counts in descending order
            sorted_restaurants = sorted(restaurant_data, key=lambda x: x[0], reverse=True)

            # Create the result message
            result_message = "*Äänestystulos*:\n\n"

            # Add restaurants with vote counts to the result message
            for i, (votes, restaurant, index) in enumerate(sorted_restaurants, start=1):
                result_message += f"{i}. {votes} ääntä: {restaurant}\n"
            if VoteMessageTs:
                
                
                #Update the previous message with the current vote count
                client.chat_update(
                channel=channel_id,
                ts=f"{VoteMessageTs}",
                text=f"{result_message}"
                )
                
                
            else:
                # Post a new message and store the timestamp in VoteMessageTs
                vastaus = client.chat_postMessage(
                channel='#lunch-bot',
                text=f"{result_message}",
                VoteMessageTs = vastaus['ts'])


@app.action("vote_click1")
def action_button_click3(body, ack):
    
    ack()
    user_id = body['user']['id']
    if user_id in voter_ids1:
        voter_ids1.remove(user_id)
    else:
        voter_ids1.append(user_id)

    äänestys()
@app.action("vote_click2")
def action_button_click3(body, ack):
    
    ack()
    user_id = body['user']['id']
    if user_id in voter_ids2:
        voter_ids2.remove(user_id)
    else:
        voter_ids2.append(user_id)

    äänestys()
@app.action("vote_click3")
def action_button_click3(body, ack):
    
    ack()
    user_id = body['user']['id']
    if user_id in voter_ids3:
        voter_ids3.remove(user_id)
    else:
        voter_ids3.append(user_id)
        
    äänestys()
@app.action("vote_click4")
def action_button_click3(body, ack):
    
    ack()
    user_id = body['user']['id']
    if user_id in voter_ids4:
        voter_ids4.remove(user_id)
    else:
        voter_ids4.append(user_id)
        
    äänestys()

@app.action("vote_click5")
def action_button_click3(body, ack):
    
    ack()
    user_id = body['user']['id']
    if user_id in voter_ids5:
        voter_ids5.remove(user_id)
    else:
        voter_ids5.append(user_id)
        
    äänestys()

@app.action("vote_click6")
def action_button_click3(body, ack):
    
    ack()
    user_id = body['user']['id']
    if user_id in voter_ids6:
        voter_ids6.remove(user_id)
    else:
        voter_ids6.append(user_id)
        
    äänestys()
@app.action("vote_click7")
def action_button_click3(body, ack):
    
    ack()
    user_id = body['user']['id']
    if user_id in voter_ids7:
        voter_ids7.remove(user_id)
    else:
        voter_ids7.append(user_id)
        
    äänestys()

@app.action("vote_click8")
def action_button_click3(body, ack):
    
    ack()
    user_id = body['user']['id']
    if user_id in voter_ids8:
        voter_ids8.remove(user_id)
    else:
        voter_ids8.append(user_id)
        
    äänestys()

@app.action("vote_click9")
def action_button_click3(body, ack):
    
    ack()
    user_id = body['user']['id']
    if user_id in voter_idsMuu:
        voter_idsMuu.remove(user_id)
    else:
        voter_idsMuu.append(user_id)
        
    äänestys()




        
        
     
                

        
   
    
    
    




if __name__ == "__main__":
    ruokanaTänään()
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

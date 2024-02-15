from bs4 import BeautifulSoup 


from pathlib import Path



import requests







def find_ruoka1():
    #HTML TEXT OF THE MENU PAGE
    html_text = requests.get('https://www.lounaat.info/lounas/cafe-hullu-orava/lappeenranta').text
    #Checking HTML page
    soup = BeautifulSoup(html_text,'lxml')
    #FIND ALL LI, MENU-LIST_ITEM, because that's where the menu content is found
    datas1 = soup.find_all('div', class_="item")
    return datas1
    
def find_ruoka2():
    #HTML TEXT OF THE MENU PAGE
    html_text = requests.get('https://www.lounaat.info/lounas/pancho-villa/lappeenranta').text
    #Checking HTML page
    soup = BeautifulSoup(html_text,'lxml')
    #FIND ALL LI, MENU-LIST_ITEM, because that's where the menu content is found
    datas2 = soup.find_all('div', class_="item")
    return datas2

def find_ruoka3():
    #HTML TEXT OF THE MENU PAGE
    html_text = requests.get('https://wolkoff.fi/ruoka-juoma/').text
    #Checking HTML page
    soup = BeautifulSoup(html_text,'lxml')
    #FIND ALL LI, MENU-LIST_ITEM, because that's where the menu content is found
    datas3 = soup.find_all('li', class_="menu-list__item")
    return datas3

def find_ruoka4():
    #HTML TEXT OF THE MENU PAGE
    html_text = requests.get('https://www.lounaat.info/lounas/httpskolmekiveafiravintolawillhelmiina/lappeenranta').text
    #Checking HTML page
    soup = BeautifulSoup(html_text,'lxml')
    #FIND ALL LI, MENU-LIST_ITEM, because that's where the menu content is found
    datas4 = soup.find_all('div', class_="item")
    return datas4

def find_ruoka5():
    #HTML TEXT OF THE MENU PAGE
    html_text = requests.get('https://www.lounaat.info/lounas/lounaskahvila-elsi/lappeenranta').text
    #Checking HTML page
    soup = BeautifulSoup(html_text,'lxml')
    #FIND ALL LI, MENU-LIST_ITEM, because that's where the menu content is found
    datas5 = soup.find_all('div', class_="item")
    return datas5

def find_ruoka6():
    #HTML TEXT OF THE MENU PAGE
    html_text = requests.get('https://www.lounaat.info/lounas/kehruuhuone/lappeenranta').text
    #Checking HTML page
    soup = BeautifulSoup(html_text,'lxml')
    #FIND ALL LI, MENU-LIST_ITEM, because that's where the menu content is found
    datas6 = soup.find_all('div', class_="item")
    return datas6



    

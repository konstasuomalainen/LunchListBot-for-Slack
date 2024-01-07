

from bs4 import BeautifulSoup 


from pathlib import Path



import requests







def find_ruoka1():
    #RUOKALISTA SIVUN KOKO HTML TEKSTI
    html_text = requests.get('https://www.lounaat.info/lounas/cafe-hullu-orava/lappeenranta').text
    #SIVULLE TEHTIIN JOTAIN XD
    soup = BeautifulSoup(html_text,'lxml')
    #LÖYDETÄÄN KAIKKI LI, MENU-LIST_ITEM, koska sieltä löytyy ruokalistan sisältö
    datas1 = soup.find_all('div', class_="item")
    return datas1
    
    
    

def find_ruoka2():
    #RUOKALISTA SIVUN KOKO HTML TEKSTI
    html_text = requests.get('https://www.lounaat.info/lounas/pancho-villa/lappeenranta').text
    #SIVULLE TEHTIIN JOTAIN XD
    soup = BeautifulSoup(html_text,'lxml')
    #LÖYDETÄÄN KAIKKI LI, MENU-LIST_ITEM, koska sieltä löytyy ruokalistan sisältö
    datas2 = soup.find_all('div', class_="item")
    return datas2

def find_ruoka3():
    #RUOKALISTA SIVUN KOKO HTML TEKSTI
    html_text = requests.get('https://wolkoff.fi/ruoka-juoma/').text
    #SIVULLE TEHTIIN JOTAIN XD
    soup = BeautifulSoup(html_text,'lxml')
    #LÖYDETÄÄN KAIKKI LI, MENU-LIST_ITEM, koska sieltä löytyy ruokalistan sisältö
    datas3 = soup.find_all('li', class_="menu-list__item")
    return datas3
    

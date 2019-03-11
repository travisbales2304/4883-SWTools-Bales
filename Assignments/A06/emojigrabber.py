"""
Course: cmps 4883
Assignemt: A06
Date: 3/10/19
Github username: travisbales2304
Repo url: https://github.com/travisbales2304/4883-SWTools-Bales
Name: Travis Bales
Description: 
    Goes to a specific website and gathers all the links to the emojies and saves them to a file in the
    working directory called Emojis
"""
from beautifulscraper import BeautifulScraper
import requests
import os


scraper = BeautifulScraper()

final_directory = os.path.join(os.getcwd(), r'Emojis')
if not os.path.exists(final_directory):
    os.makedirs(final_directory)


url = 'https://www.webfx.com/tools/emoji-cheat-sheet/'
page = scraper.go(url)


for emoji in page.find_all("span",{"class":"emoji"}):
    image_path = emoji['data-src']
    print(url+image_path)
    i = requests.get(url+image_path)
    file = open(os.path.join('Emojis/',image_path.split('/')[-1]),"wb")
    file.write(i.content)






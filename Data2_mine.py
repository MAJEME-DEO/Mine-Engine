import requests
import json
import urllib.parse
from bs4 import BeautifulSoup as Soup

main_api = 'https://api.github.com/search/repositories?q'

while True:
    address = input('Address: ')

    if address == 'quit' or address == 'q':
        break
    my_url = main_api + urllib.parse.urlencode({'': address})
    print(my_url)
    uData = requests.get(my_url).json()
    print(type(uData))

    with open('personal1.json', 'w') as json_file:
        json.dump(uData, json_file)
#    uData.close()
""""
    # html parsing
    data_soup = Soup(uData, 'html.parser')
    print(data_soup)
    type(data_soup)
"""

import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.fasching.se/?date=0&artist=all&view=default&c=20")
fasching_page = response.text

#print(fasching_page)




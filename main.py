import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.fasching.se/?date=0&artist=all&view=default&c=20")
fasching_page = response.text

soup = BeautifulSoup(fasching_page, "html.parser")

artists_select = soup.find("select", class_="sort__select")
artists_options = artists_select.find_all("option")
artists_trimmed = artists_options.pop(0)
option_values = []

for a_o in artists_options:
    option_values.append(int(a_o["value"]))

#print(artists_options)

print(option_values)




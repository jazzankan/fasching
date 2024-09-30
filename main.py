import requests
from bs4 import BeautifulSoup
import json

response = requests.get("https://www.fasching.se/?date=0&artist=all&view=default&c=20")
fasching_page = response.text

soup = BeautifulSoup(fasching_page, "html.parser")

artists_select = soup.find("select", class_="sort__select")
artists_options = artists_select.find_all("option")
artists_options.pop(0)
option_values = []

for a_o in artists_options:
    option_values.append(int(a_o["value"]))

with open('valuefile.json', 'r') as f:
    old_values_list = json.load(f)

print('\nNya konserter:')
for o in option_values:
    if o not in old_values_list:
        for art_opt in artists_options:
            if art_opt['value'] == str(o):
                print(art_opt.get_text())

with open('valuefile.json', 'w') as f:
    json.dump(option_values,f)





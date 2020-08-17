import requests
from bs4 import BeautifulSoup
# allegheny service berry 
url = "https://tree-map.nycgovparks.org/tree-map/species/3133"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
#soupStr = soup.text
#print(soupStr)

divList = []

table = soup.findAll('div', attrs={"class": "EcologicalBenefits_benefits__3Aruf"})

print(table)

#for x in table:
 #   divList.append(x.find('span').text)
    
#print(divList)

vals = [d.text for d in table]
print(vals)
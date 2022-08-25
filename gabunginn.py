import requests
import simplejson
from bs4 import BeautifulSoup
from datetime import datetime

req = requests.get('https://republika.co.id/')

obj = BeautifulSoup(req.text,"html.parser")

print("----Menampilkan Semua Teks Headline----")
print("=======================================")


file = open(r'https://aryadipura.github.io/WebScrap/headline.txt','w')
for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
    file.write(headline.find('h2').text)
    file.write('\n')
file.close()

file = open(r'https://aryadipura.github.io/WebScrap/headline.txt','r')
for f in file:
    print(f)
file.close()

data = []

# Extract Data From div class="bungkus_txt_headline"
terkini = obj.find_all('div',class_='conten1')
f=open(r'https://aryadipura.github.io/WebScrap/headline.json','w')
for article in terkini:
    title = article.find('h2').text
    category = article.find('h1').text
    publish = article.find('div',class_='date').text
    now = datetime.now()
    date = now.strftime("%d %B %Y %H:%M:%S")

    data.append({"title":title, "category":category, "publish":publish, "date":date})

print("JSON Updated")
jdumps = simplejson.dumps(data)
f.writelines(jdumps)
f.close
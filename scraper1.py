import requests
from bs4 import BeautifulSoup
import json
import shutil
import os
import glob


files = glob.glob('fasad/*')
for f1 in files:
    os.remove(f1)


f2 = open('product.txt', 'w')
f2.write('')
f2.close()

url = 'https://maxmaster.ru/smennye-lezviya-dlya-nozhey/page-4/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='ut2-gl__body')

f = open('product.txt', 'r+')

for n, i in enumerate(items, start=1):
    itemName = i.find('a', class_='product-title').text.strip()
    data = itemName.split(' ',1)
    x = data[0]
    y = data[1]
    itemPrice = i.find('span', class_='ty-price-num').text
    itemPrice = itemPrice.replace(" ", "")
    z = float(itemPrice) + (float(itemPrice) * 0.40)



    image = i.find_all('img', class_='cm-image')
    poster_link = []
    for img in image:
        poster_link.append(img.get('data-src'))


    posterString = ''.join(poster_link)
    filename = posterString.split("/")[-1]

    r = requests.get(posterString, stream = True)
    with open('fasad/'+filename,'wb') as t:
        shutil.copyfileobj(r.raw, t)


    f.write('''<div class="col-md-3 col-6">
      <div class="product-wrap border1">
        <div class="product-item ">
          <img src="{% static 'img/lomi/''' +filename+ ''''%}">
          <div class="product-buttons">
            <a href="" class="button">Перейти</a>
          </div>
        </div>
        <div class="product-title">
          <a href="">'''+x+'''</a>
        </div>
        <div class="product-price1">'''+y+'''</div>
        <span class="product-price">'''+str(int(z))+''' руб</span>
      </div>
    </div>''' + "\n")

f.close()




# ''' +filename+ ''''

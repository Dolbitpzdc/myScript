import requests
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


slice = "4"
# slice='+slice+'&
url = 'https://store.tildacdn.com/api/getproductslist/?storepartuid=316134531891&recid=288356163&c=1622815660472&getparts=true&getoptions=true&slice='+slice+'&size=16'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
}
response = requests.get(url, headers=headers)

x = json.loads(response.text)

f = open('product.txt', 'r+')

for product in x['products']:
    y = float(product['price']) + (float(product['price']) * 0.20)

    image = json.loads(product['gallery'])[0]['img']
    filename = image.split("/")[-1]

    r = requests.get(image, stream = True)
    with open('fasad/'+filename,'wb') as t:
        shutil.copyfileobj(r.raw, t)

    f.write('''<div class="col-md-3 col-6">
      <div class="product-wrap border1">
        <div class="product-item ">
          <img src="{% static 'img/fasad/''' +filename+ '''' %}">
          <div class="product-buttons">
            <a href="" class="button">Перейти</a>
          </div>
        </div>
        <div class="product-title">
          <a href="">'''+product['title']+'''</a>
        </div>
        <span class="product-price">'''+str(int(y))+''' руб/м2</span>
      </div>
    </div>''' + "\n")

f.close()

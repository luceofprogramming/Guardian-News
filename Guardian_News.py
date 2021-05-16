#1
import sqlite3
import requests
import json
url = 'https://content.guardianapis.com/search?api-key=cdc574f8-f9f3-4556-b0e2-b213ae7a76ae'
r=requests.get(url)
result_jason=r.text
res=json.loads(result_jason)
res_structured = json.dumps(res, indent=4)
m=res['response']
status_code= m['status']
print(status_code)
test=m['results']
a=int(input("შეიყვანეთ რიცხვი თუ რომელი სტატიის თემატიკა გაინტერესებთ"))

test=test[a-1]
header=test['webTitle']
print(f'სტატია N{a}-ის სათაურია {header} ')
print(res_structured)
print(len(res['response']['results']))

#2
info = r.json()
with open('news.json', 'w') as newspaper:
    json.dump(info, newspaper, indent=4)
#3
#ბაზაში ჩამატება:
#ცხრილში თავმოყრლია მცრე ინფო სტატიიებისშესახებ,როგორიცაა მისი სათაური,ნუმერიფიკაცია და სექციიის დასახელება
conn = sqlite3.connect("News.sqlite")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE Articles
(id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR,
order INTEGER ,
sectionName VARCHAR );''')
for x in range(0, 10):
    title = (res['response']['results'][x]['webTitle'])
    order = x+1
    sectionName = (res['response']['results'][x]['sectionName'])
    cursor.execute('INSERT INTO Articles (title, order, sectionName) VALUES (?, ?, ?)',
                   (title, order, sectionName ))
    conn.commit()

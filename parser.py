#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup as BS
import json
#장고에 추가하기---
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","main.settings")
import django
django.setup()
#main_Crwaling data 집어넣기
from main_Crawling.models import Crawling


req = requests.get('https://www.timeticket.co.kr/list.php')
 
html = BS(req.text, 'html.parser', from_encoding='utf-8')

tr_list = html.find('div',{'id':'zlist'}).find_all('td',{'valign':'top'})

def main_Crawling(html) :

    temp_list = []
    temp_dict = {}
    id = -1 
    # data = {}
    for tr in tr_list :
        id += 1
        area = tr.find('span',{'class':'category_rows_area'}).text
        title = tr.find('span',{'class':'category_rows_title'}).text
        sale = tr.find('td',{'class':'category_rows_sale'}).text.strip()
        price = tr.find('td',{'class':'category_rows_price'}).text
        img = tr.find('img')
        img_src = img.get('src')
        # print(img_src,area,title,sale,price) 
        # temp_list.append([img_src,area,title,sale,price])
        temp_dict[str(id)] = {'img_src':img_src, 'area':area, 'title':title,
                    'sale':sale, 'price':price}
        # data[tr.area] = 1
    
    return temp_dict
    
#================================#
def toJson(main_dict):
    with open('main.json', 'w', encoding='utf-8') as file:
        json.dump(main_dict,file,ensure_ascii=False, indent='\t')
#================================#
#가격 td class category_rows_price
#할인율 td class categoty_rows_sale
#지역 span class category_rows_area
#제목 span class category_rows_title
#이미지 img class ticket-poster

main_list = []
main_dict = []


main_dict = main_Crawling(html)


# for item in main_dict :
#      Crawling(item, main_dict[item]['img_src'],main_dict[item]['area'],main_dict[item]['title'],
#         main_dict[item]['sale'],main_dict[item]['price']).save()
for item in main_dict :
     Crawling(item, main_dict[item]['title'],main_dict[item]['area'],main_dict[item]['sale'],
        main_dict[item]['price'],main_dict[item]['img_src']).save()



# for a,b,c,d,e in main_dict :
    #  Crawling(area=a,title=b,sale=c,price=d,img_src=e).save()

# toJson(main_dict)
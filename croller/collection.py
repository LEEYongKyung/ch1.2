import time

from bs4 import BeautifulSoup
from itertools import count
from pandas import DataFrame
from selenium import webdriver
from datetime import datetime

from crawler import crawling
# import datetime

def crawling_pelicana():
    results = []
    for page in count(1,):
        html = crawling('https://pelicana.co.kr/store/stroe_search.html?branch_name=&gu=&si=&page=%d' %page)
        # print(html)
        bs = BeautifulSoup(html, 'html.parser')

        tag_table = bs.find('table',attrs={'class':'table mt20'})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        #끝페이지 검출
        if len(tags_tr) == 0 :
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings) # 태그 안의 데이터를 string list로 추출 문자로 개행별로 추출
            name = strings[1]
            address = strings[3]
            # print(name,address)
            sidogu = strings[3].split()[:2]
            # t = (name, )+tuple(sidogu)
            results.append((name, )+tuple(sidogu))

    print(results)

    #store
    table = DataFrame(results, columns=['name','sido','gugun'])
    table.to_csv('results/table_pelicana.csv',encoding='utf-8',mode='w',index=True)
    print(table)



def crawling_nene():
    results = []
    first_shopname_prevpage = ''
    for page in count(start=1):
        html = crawling('https://nenechicken.com/17_new/sub_shop01.asp?page={page}&ex_select=1&ex_select2=&IndexSword=&GUBUN=A'.format_map({'page':page}))
        # print(html)
        bs = BeautifulSoup(html,'html.parser')

        tag_div = bs.find('div',attrs='shopWrap')
        tags_div_shop = tag_div.findAll('div', attrs = {'class':'shopInfo'})
        # 끝페이지 검출
        shopname = tags_div_shop[0].find('div', attrs={'class': 'shopName'}).text
        if first_shopname_prevpage == shopname:
            break

        first_shopname_prevpage = shopname
        for tag_div_shop in tags_div_shop:

            name = tag_div_shop.find('div', attrs = {'class': 'shopName'}).text
            address = tag_div_shop.find('div', attrs={'class': 'shopAdd'}).text
            sidogu = address.split()[:2]
            results.append((name, )+ tuple(sidogu))


            # name = strings[1]
            # address = strings[3]
            # # print(name,address)
            # sidogu = strings[3].split()[:2]
    print(results)

    # store
    table = DataFrame(results, columns=['name', 'sido', 'gugun'])
    table.to_csv('results/table_nene.csv', encoding='utf-8', mode='w', index=True)



def crawling_kyochon():
    # for sido1 in range(1,18):
    results = []
    for sido1 in range(1,18):
    # for sido1 in range(1, 2):
        for sido2 in count(start=1):
        # for sido2 in range(1,2):
            url = 'http://www.kyochon.com/shop/domestic.asp?sido1=%d&sido2=%d&txtsearch=' %(sido1,sido2)
            html = crawling(url)
            if html is None: #범위를 벗어난 것은 exception되면서 None
                break

            # print(html)
            bs = BeautifulSoup(html, 'html.parser')
            tag_ul = bs.find('ul',attrs={'class':'list'})
            tags_a = tag_ul.findAll('a')

            for tag_a in tags_a:
                # print(tag_a)
                tag_strong = tag_a.find('strong')
                if tag_strong is None:
                    break
                name = tag_strong.text
                strings =list(tag_a.find('em').strings)
                print(strings)
                address = strings[0].strip('\r\n\t')
                sidogu = address.split()[:2]
                t = (name, ) + tuple(sidogu)
                results.append(t)
                # print(name, address)
                # print(strings)
                # print('==============================================')
    print(results)

    # store
    table = DataFrame(results, columns=['name', 'sido', 'gugun'])
    table.to_csv('results/table_kyochun.csv', encoding='utf-8', mode='w', index=True)

def crawling_goobne():
    url = 'http://www.goobne.co.kr/store/search_store.jsp'

    #첫 페이지 로딩
    wd =webdriver.Chrome('D:\PythonStudy\chromedriver.exe')
    wd.get(url)
    time.sleep(2)
    results = []
    for page in count(start=1):
        #자바 스크립드 실행
        script = 'store.getList(%d)' %page
        wd.execute_script(script)
        print('%s : success for script execute[%s]'%(datetime.now() ,script)  )
        time.sleep(2)

        #실행결과 (랜더링된 결과 )HTML 가져오기
        html = wd.page_source
        # print(html)
        #parsing with bs4
        bs = BeautifulSoup(html, 'html.parser')
        tag_tbody = bs.find('tbody',attrs={'id':'store_list'})
        tags_tr = tag_tbody.findAll('tr')

        #마지막 검출
        if tags_tr[0].get('class') is None:
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[6]
            sidogu = address.split()[:2]

            results.append(((name,)+tuple(sidogu)))
    print(results)

    # store
    table = DataFrame(results, columns=['name', 'sido', 'gugun'])
    table.to_csv('results/table_goobne.csv', encoding='utf-8', mode='w', index=True)

if __name__ == '__main__':
    #perlicana collections
    crawling_pelicana()

    crawling_nene()

    #kyochon collection
    crawling_kyochon()

    #goobne collection
    crawling_goobne()
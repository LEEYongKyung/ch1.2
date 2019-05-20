from bs4 import BeautifulSoup
from itertools import count
from pandas import DataFrame
from crawler import crawling
import datetime

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





if __name__ == '__main__':
    #perlicana collections
    crawling_pelicana()
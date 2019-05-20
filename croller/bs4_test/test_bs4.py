from bs4 import BeautifulSoup


html = '<td class="title black"><div class="tit3" id="div-title"> \
        <a href="/movie/bi/mi/basic.nhn?code=174065" title="걸캅스">걸캅스</a></div></td>'

#1.조회

def ex1():
    bs = BeautifulSoup(html,'html.parser')
    print(bs)

    tag = bs.a #태그별로 조회 a 태그 조회
    print(tag, type(tag))
    print(tag.name) #element 정보르 알려줌


#2. 속성 attribute 가져오기

def ex2():
    bs = BeautifulSoup(html, 'html.parser')
    tag = bs.td
    print(tag['class']) #여러 class 아이디를 가져올 수 있음

    tag = bs.div
    # 없는 속성을 가져오면 error가 난다.
    print(tag['id'])
    print(tag.attrs) # class는 여러 이름으로 가능하니 list로 id는 하나 박에서 안되서 하나만

#3. Attribute 조회

def ex3():
    bs = BeautifulSoup(html, 'html.parser')
    tag = bs.find('td',attrs={'class':'title'})
    print(tag)

    tag = bs.find(attrs={'title':'걸캅스'})
    print(tag)

    tag = bs.find('td')
    print(tag)



if __name__=="__main__":
    # ex1()
    # ex2()
    ex3()



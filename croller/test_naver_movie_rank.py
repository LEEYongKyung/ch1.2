from urllib.request import Request, urlopen
from  bs4 import BeautifulSoup

request = Request('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
resp = urlopen(request) #Req보내고 응답이 옴
html = resp.read().decode('cp949') #byte단위로 인코딩 되므로 디코딩 필요 euc-kr로 코드가 되엉 ㅣㅆ어서 cp949디코딩
print(html)

bs = BeautifulSoup(html,'html.parser')
print(bs.prettify()) # 코드를 예쁘게 정리

tags = bs.findAll('div', attrs={'class':'tit3'}) # findAll 해당 되는걸 모두 다 찾음  #find는 하나만
# print(tags)
for index ,tag in enumerate(tags) :
    print(index+1, tag.a.text, tag.a['href'], sep= ' : ') # 내용 가져오는건 text a태그의 내용 출력

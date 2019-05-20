import ssl
from datetime import datetime
from urllib.request import Request, urlopen


def crawling(url='', encoding ='utf-8') : # deault값 설정
    try:
        request = Request(url)

        #HTTPS 접근 VERFIY못하도록 해서 접근
        ssl._create_default_https_context = ssl._create_unverified_context


        resp = urlopen(request)  # Req보내고 응답이 옴
        try:
            receive = resp.read()

            result = receive.decode(encoding)
        except UnicodeDecodeError:
            result = receive.decode(encoding,'replace')

        print('%s:successs for request(%s)' % (datetime.now(),url))
        return result
    except Exception as e:
        print('%s : %s' % (e, datetime.now()))
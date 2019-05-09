#한 줄 문자열
s = ''
str1 = 'Hello world'
str2 = "HEllo World"
print(type(s),type(str),type(str1))
print(isinstance(str2,str))

#여러 줄 문자열
str3 = """  ABC
DEF
가나다라마바사
아자차카타파하
"""
print(str3)

#여러줄 주석 => 여러줄 문자열을 사용한다.
"""
주석1
주석2

"""

#escape
print("hello \nworld\n ")
print("I Say \"HELLO\'")
print("I Say 'HELLO'")
print('She\'s Mom')
print("둘리\t010-0000-0000")

#문자열 연산
str1 ='First String'
str2 = 'Second String'
str3 = str1 + ' ' + str2
print(str3)

#반복
str4 = str1*3
print(str4)

#indexing
print(str1[0], str1[2], str1[4])

#슬라이싱
str5 = str2[2:5]
print(str5)
print(str2[2:])

#연결(+) , +는 생략 가능

str3 = str1 + ' ' +str2
str6 = 'hello' ' - ' 'World'
print(str6)

# 문자열 객체와 정수형 객체 +연산을 할 수 없다.
name = 'LEE'
ages = 40
print(name+str(ages))


#len() 문자열 길이 함수
print(len(str2))

#in, not in 연산
print("S" in str2)
print("S" not in str2)

#문자열 객체는 변경 할 수 없다.[imutable]
# str1[0] = 't'
# print(str1)


#formating (서식) - tuple
f = "name:%s, age:%d"

print(f)
print( f % ('LEE',10)) #tuple을 이용한 서식
print( f % ('Yong',20)) #tuple을 이용한 서식


#formating (서식) - format() 함수
name = '마이콜'
ages = 30
print("name:"+name+"age: "+str(ages))
print("name:"+name+"age: "+format(ages,"d"))
print("name:"+format(name,'s')+"age: "+format(ages,"d"))

# 대소문자 관련 객체함수
s = 'i like PYTHON'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize()) #맨 앞에 문자를 대문자로 변환
print(s.title())# 각 문자의 앞자리만 대문자


#검색 관련 객체함수
s = 'I Like Python, I Like Java'
print(s.count('Like')) #해당 문자 개수
print(s.find('Like'))
print(s.find('Like',5)) #find의 시작 위치를 지정
print(s.find('JAVASCtipy'))
print(s.rfind('Like')) #뒤에서 부터 찾음

#발견하지 못하면 예외가 발생
print(s.index('Like')) #find와 비슷 find는 못찾으면 -1이 나오고(ㅍProcess finished with exit code 0)
#print(s.index('Likeㅇㄿㅇ')) #index는 못찾으면 exceoption이 발생 (Process finished with exit code 1)

print((s.rindex('Like')))

# 해당 객체가 해당문구로 시작하는가를 판별 True, False로 반환
print(s.startswith('I Like'))
#두번째부터 시작하는가
print(s.startswith('I Like',2))

#끝나는것
print(s.endswith('Also'))
print(s.endswith('Java', 0, 26)) #검색 범위 지정

#편집, 치환
# 웹에서 이메일등의 데이터를 받을때 사용자가 본인도 모르게 공백을 넣을 수있어서ㅓ
s = '      spam and has                   '
print('-------'+s.strip()+'-----------') #앞뒤에 공백을 제서
print('-------'+s.rstrip()+'-----------')
print('-------'+s.lstrip()+'-----------')  #

print('-------'+s.strip('<>')+'-----------')


s = 'HELLO JAVA'

print(s.replace('JAVA', 'PYTHON'))

#정렬
s = 'King and Queeea'
print('----'+s.ljust(20)+'----')
print('----'+s.rjust(20)+'----')


#분리
s = "SPAM AND HAM"
r = s.split(' AND ') #and를 가지고 분리 return 리스트 아니면 튜블로 리턴
print(r)

s = 'one:two:three:four'
r = s.split(':')
print(r)

r = s.split(':',2) #2개의 리스트 로 구분 나머지는 합쳐서 하나로
print(r)

r = s.rsplit(':',2) #위의 것과 반대 순서로 분리
print(r)


lines = """1st line
2nd line
3nd line
4nd line
"""
print(lines)
lines = """1st line
2nd line
3nd line
4nd line
"""

print(lines)

r = lines.split('\n')
print(r)

# r = lines.splitlines('\n') #빈 스트링은 배열에 담지않고 line별로 리스트에 담
# 음
print(r)
#결합
s= '.'.join(r) #배열을 '.'문자로 합쳐라 str형으로 반환 특정 리스트를 결합
print(s)

#판별

print('1234'.isdigit())
print('ABCD'.isalpha())


print('1234'.isalpha())
print('ABCD'.isdigit())


print('1234A'.isalpha()) # False 완전 숫자거나 완전 문자일때만 True가능
print('ABCD1'.isdigit())

print('abcd'.islower())
print('ABCD'.isupper())

print(' '.isspace())
print('\n'.isspace()) #개행도 space로 처리
print('\t'.isspace()) #개행도 space로 처리

# 0 채우기
print(str('1').zfill(5)) #zero fill
print(str('9234').zfill(5)) #zero fill

#formating 서식
# 기존 전역 함수가 아닌 객체함수로서의 format

f = 'name:{}, age:{}'
s = f.format("둘리",30)
print(s)

f = 'name:{1}, age:{0}'
s = f.format(10,"둘리")
print(s)


print('name:{}, age:{}'.format("둘리",10))
print('name:{0}, age:{1}'.format("둘리",10))
print('name:{1}, age:{0}'.format(10,"둘리"))

f = 'name:{n}, age:{a}'
s = f.format_map({'n':'둘리', 'a':10}) #dictionary형
print(s)


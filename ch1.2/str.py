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






# 치환문
a = 1
b = a + 1
# 변수가 없는 값을 literal이라 하낟.
print(a, b) # 가변 변수 함수의 값이 정해 지지 않음
print(a, b, sep=  ' ') # default변수가 가운데space를 가지고 있다.
print(a, b, sep=  ' : ') # default변수가 가운데space를 가지고 있다.

# 세미클론으로 치환문을 구분 가능




#여러개 한거번에 치환
e, f = 3.5, 5.3 # tuple의 형태로 변수 값 지ㄱ정이 가능
print(e, f)

#같은 값을 여러변수에 할당

x = y = z = 10

print(x, y, z)

# c 스타일은 지원 하지 않는다.

# x = (y = 10) #소괄호는 tuple의 자료형을 표현하기 때문에 (tuple literal) 사용 불가능

#swap
x, y =1, 2
tmp = x
x = y
y=tmp
print(x, y)


c, r = 1, 2 #간단 치환

c, r = r, c
print(c, r)


#동적 타이핑
a = 1
print(type(a))

a = 'hello'
print(type(a))


#확장 치환문
a = 10
a += 10
print(a)

a -= 3
print(a)
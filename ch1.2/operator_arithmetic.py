# 사칙연산
print(2*3)
print(2+3)
print(2-3)
print(2/3)
print(2/3.0)


# //(몫 연산자) **(지수승) %(나머지 연산)

print(2//3)
print(2**3)
print(2%3)


#divmode() 함수
print(divmod(2,3))#값이 튜블로 나옴

t = divmod(2,3)

print(type(t))

a,b = divmod(2,3)  # tuple의 값을 나누면서 tuple unpacking
print(a, b, type(a), type(b))


#연산자 우선순위
print(2+3*4)
print(-2+3*4)
print((-2+3)*4)

#결합순서
print(2 ** 3 ** 4) # <---순서로 연산이 진행됨
print((2 ** 3) ** 4) # <---순서로 연산이 진행됨


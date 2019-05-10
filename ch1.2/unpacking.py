#packing은 tuple로만 가능

t = 10,20,30,'python'
print(t, type(t))

#unpacking
a,b,c,d = t
print(a,b,c,d)

#오류나는 경우 : 패킹되어 있는 객체가 변수보다 더 많은 경우
# a,b,c = t

#오류나는 경우 : 패킹되어 있는 객체가 더 적은 경우
# a,b,c,d,e = t

#unpacking 변수 갯수를 안맞춰도 되는 경우
t = (1,2,3,4,5)
a,*b= t #'*'를 통해 여러개 들어갈수 있다는 것을 표시 b변수에 나머지 데이터 들이 list로 들어감
print(a,b)

*a,b =t
print(a,b)



a,b,*c =t
print(a,b,c)


# 튜플을 이용해서 여러개의 값을 대입할 수 있다.
x,y,z = 10,20,30

# 튜플을 이용해서 여러개의 값을 치환할 수 있다.
x,y = 10,20


#
# 객체 함수 : imutable 떄문에 객체 함수가 많지 않다.
#
t = (20,30,40,50,20)
print(t.index(30))
print(t.count(20))


#변환 (tuple -> set)
s = set(t)
print(s)
#변환 (tuple -> list)
l = list(t)
print(l, type(l))

#변환 ( list -> tuple)
tu = tuple(l)
print(tu, type(tu))
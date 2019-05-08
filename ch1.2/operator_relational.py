# 객체의 대소 비교

print(1>3) # 각 값을 연산하고 난 후엔 값이 모두 없어진다. 왜냐면 각 값을 저장하는 객체 지정이 없으므로 사라져 버린다.
# 값을 계속 가지고 있기 위해선 객체로 저장해야한다. a=1
print(2>4)


print(1>=3)
print(2>=4)


#복합 관계식 지원(파이선만 지원)
a=6
print(0<a and a<10) #다른언어에서 표현시

print(0<a<10) #파이선에서 사용시

#수치형 이외의 다른 타입의 개체도 비교 가능

print('abcd '>'abc')
print((1,2,3)>(1,2,2))
print([1,2,3]>[1,2,2])

#동질성 비교 ==
#동일성 비교 is

a = 10
b = 20
c = a

print(a == b)
print(a is b)
print(a == c)
print(a is c)


# == 동질성 : 값이 같은가
# is 동일성  : 가리키고 있는 객체가 같은가.
# == 과 is는 리스트 비교를 통해  두개의 특성을 구분할 수 있다.
# a= [1,2,3] 이고 b= [1,2,3] 일때 두개의 동일성은 서로 다른 객체를 가리키고 있으니 다를 것이나 그러나 두 리스트의 값들은 같으므로 동질성은 같게 된다.
a =40
print(a == c)
print(a is c)

lis1 = [1,2,3]
lis2 = [1,2,3]
print('동질성',lis1 == lis2)
print('동일성',lis1 is lis2)

print(True or 'logical') #True 출력: OR 연산의 논리식에 따라 앞에서 True이면 뒤를 따로 볼 필요가 없어서 True 출력
print(False or 'logical') # logical 출력
print([] or 'logical')  #[] 빈 배열은 0으로 취급
print([10, 20] or 'logical')  #[] 빈 배열은 0으로 취급

print('operator'or 'logical')  #'operator'가 True로 취급
print('' or 'logical')
#파이선에서 OR연산은 앞에가 무조건 boolean이어야 하므로

#None : 가지고 있는 객체가 없다.

print(None or 'logical')
print(None or [])

s = 'Hello World'
s and print(s)

s = ''
s and print(s) #아무것도 출력되지 않음


#LIST
#list 생성
l = []
l = [1,True,'Python',3.14]

#indexing
print(l[0],l[1],l[2],l[3])
print(l[-4],l[-3],l[-2],l[-1]) #마이너스 indexing은 순서가 반대이다. 이건 리스트 스트링 튜플 모두 같다.

#slicing
print(l[1:3]) # default 모습은 print(l[1:3:1])이다 1이상 3미안 까지 1씩 커지는 것이다.
print(l[2:4])
print(l[3::-1]) #1실 줄어듬
print(l[len(l)-1::-1]) #1실 줄어듬


#반복
l2 = l *2
print(l2)


#연결
l2 = l + [1,2,3]
print(l2)

#길이
print(len(l))

#객체가 들어있는 지 확인
print(5 in l2)
print('Python' in l2)

#삭제 변경 가능한 객체다
del l2[2]
print(l2)

#변경 가능한 객체(mutable)
a = ['apple', 'banana',10,20]
a[2] = a[2]+90
print(a)

# 슬라이싱을 사용한 치환
a = [1,12,123,1234]
a[0:2] = [10,20]
print(a)

a[0:2] = [100] #리스트 인수가 하나 줄어들게 치환
print(a)

a[1:2] = [200]
print(a)

a[2:3] = [300,400]
print(a)

# 슬라이싱을 사용한 삭제
a = [1,12,123,1234]

a[1:2] = []
print(a)

a[0:] = []
print(a)
#
# 슬라이싱을 사용한 삽입
#
a = [1,12,123,1234]

# 중간삽입
a[1:1] = ['A']
print(a)

# 마지막에 삽입
a[5:] = [12345]
print(a)
a[len(a):] = [12345]
print(a)

# 맨 처음에 삽입
a[:0] = [0]
print(a)


# 여러 데이터 삽입
a[2:2] = [-12, -1, 0]
print(a)


#
# 객체함수
#
a = [1,3,4]

# 중간삽입
a.insert(1, 2)
print(a)

#맨 뒤에 삽입
a.append(5)
print(a)

#앞에 삽입
a.insert(0, 0)
print(a)

# 뒤집기 reverse
a.reverse()
print(a)

#제거 (값으로 삭제 위치로삭제가 아님)
a.remove(3)
print(a)
    #해당 값이 없는 경우 예외 발생
# a.remove(6)
# print(a)

#확장
a.extend([-1,-2,-3])
print(a)

#stack으로 사용하기
s = []

s.append(10) #push
s.append(20) #push
s.append(30) #push

print(s)
print(s.pop()) #POP
print(s.pop()) #POP
print(s)

#queue로 사용하기

q = [1,2]
q.append(3)
q.append(4)
q.append(5)

print(q)
print(q.pop(0)) #맨 앞에것을 pop
print(q.pop(0))
print(q.pop(0))
print(q)

#sort() 내장된 정렬 sorting 알고리즘에 따라 정렬
l = [1,5,3,9,8,11]
l.sort()
print(l) #정렬 완료
l.sort(reverse=True) #반대로 역 정렬
print(l)

l = [10,2,33,9,8,33,4,11]
l.sort(key = str) #string으로 정의할 것 앞에 문자를 ASC 코드값으로 변환해서 보기때문데 11보다 2가 더 크다
print(l)

l.sort(key=int)
print(l)

#전역함수 sorted()를 이용한 정렬
l = [19,46,37,28,91,55,64]
l2 = sorted(l)
print(l2)

l2 = sorted(l, reverse=True)
print(l2)


l = [19,46,37,28,91,55,64]

def f(i):
    return i % 10

l2 = sorted(l, key=f, reverse=True) #배열의 값을 키에 해당하는 연산의 결과 값으로 비교하여 순서의 반대로정렬
print(l2)


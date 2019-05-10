#집합형
#생성
s = {1,2,3}
print(s, type(s))

#기본연산
print(len(s))
print(2 in s)
print(10 not in s)

#list의 중복성 제거
nums = [1,2,3,4,2,2,5,5,6]
s = set(nums)
print(s, type(s))

nums = list(s)
print(nums)

#
#  객체 함수
#
# 추가
s.add(7)
print(s)
s.add(7)
print(s)
# 제거
s.discard(2)
print(s)
s.remove(3)
print(s)
#discard와 remove차이점은 존재하지 않는 데이터에 대해 제거할려고 할때 discard의 경우 데이터가 없으면 그냥 현상 유지 인데 remove는 예외 발생

#update
s.update({6,7,8})

print(s)

s.clear()
print(s)

#수학의 집합과 관련된 객체 함수
s1 = {1,2,3,4,5,6,7,8,9,10}
s2 = {10,20,30}
s3 = s1.union(s2) #합집합
print(s3)

s4 = s1.intersection(s2) #교집합
print(s4)

s5 = s1.difference(s2)
print(s5)

s6 = s1.symmetric_difference(s2)
print(s6)



#생성
t = () #빈 튜플
t = (1,2,3,1,2,3)

print(t, type(t))
# t = (1,) #요소가 하나짜리 tuple은 계산시 괄호로 인식하기 때문에 하나짜리 튜플은 반드시 콤마(,)를 사용한다.
# e = (1)
# print(t, type(t))
# print(e, type(e))

#
# 시퀀스 연산
#
#슬라이싱
print(t[-3],t[-2],t[-1],t[0],t[1],t[2])

#반복
t2 = t*2
print(t2)

#연결
t3 = t + (4,5,6)
print(t3)

#길이
print(len(t))

#in, not in
print(5 in t3)

#튜플은 변경 불가능 하다. (imnutable)  sequence 형
# t = ('apple','banana',10,20)
# t[2] = 90

#
# 튜플 객체 함수
#

#생성
d = {'basketball':5, 'baseball':9} #기본형
print(d, type(d))
d2 = dict() #
print(d2, type(d2))

d3 = dict(one=1, two=2, three=3, five=5)
print(d3)

# d4 = dict{[{'one',1},{'two',2},{'three',3},{'five',5}]}
# print(d4, type(d4))


#인덱스 대신에 키로 접근
print(d['baseball'])

#연결을 지원하지 않는다.

#d + {'valleyball':6} #예외 발생

# 반복(*)을 지원하지 않는다.
# d2 = d*2 #예외 발생

#크기
print(len(d))

# in, not in : 키만 가능
print('soccer' not in d)
print('baseball'  in d)


#다양한 타입의 키를 사용할 수 있다.
d = {}
print(d)

d['twenty'] = 20
d[True] = 'true'
d[10] = 10
print(d)

#키값은 변경 불가능한 타입의 값을 사용해야 한다.
# d[[1,2,3]] = 6

#
# 객체함수
#
k=d.keys()
print(d.keys(), type(d.keys()))

for key in k:
    print(key, d[key])

v = d.values()
print(v, type(v))

items = d.items()
print(items, type(items))

for t in items:
    print(t)

phones = {'둘리':'0000-0000-0000','도우넛':'1111-1111-1111','또치':'2222-2222-2222'}
p = phones
print(phones)
print(p)
phones['마이콜'] = '333-3333-3333'
print(phones)
print(p)

p = phones.copy() #p와 phones가 같은 객체를 가리키는게 아니라 그대로 복사에서 다른 객체에 저장
print(phones)
print(p)
phones['마이콜'] = '4444-4444-4444'
print(phones)
print(p) # 그래서 = 과 copy는 다름

print(p.get('마이콜'))
#get()을 사용하는 이유: 없는 경우는 None
#[]로 가져오는 경우에는 없을 시 예외 발생
# print(p['길동']) #예외 발생
# get으로 가져오는 경우에는 없을 시 None으로 되기 때문에 안전
print(p.get('길동')) #

#setDefault : get()과의 차이점은 실제로 저장이 된다. #찾아보고 데이터가 없으면 데이터 추가
print(p.setdefault('길동','5555-5555-5555'))
print(p)

#pop() : 삭제와 동시에 값을 가져온다.
phone = p.pop('둘리')
print(phone)
print(p)
#popitem(): 키와 벨류를 모두 pop 어떤게 pop될지 모름
t = p.popitem()
print(t)
print(p)

#모두 삭제
p.clear()

#조회
d = {'c':3, 'a':1, 'b':2}

for key in d:
    print(key, end='  ')
else: #for문 뒤에 else가 항상 실행이 됨
    print('\n')

print('HELLO')


for key in d.keys():
    print(key, end='  ')
else: #for문 뒤에 else가 항상 실행이 됨
    print('\n')

for key, value in d.items():
    print(key, value)

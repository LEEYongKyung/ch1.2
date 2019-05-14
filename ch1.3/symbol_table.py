def f():
    l_a = 2
    l_b = '마이콜'
    print(locals()) # local 심벌 테이블은 임시적으로 생겼다가 함수가 끝나면 사라짐

g_a = 1
g_b = '둘리'
f()
print(globals()) #global Table 보기 , 모듈의 심볼을 모두 모음


# 심벌 테이블을 가지고 있는 것들


# 1.  정의된 함수
f.k = 'hello'
print(f.__dict__)


class MyClass:
    x=10
    y=20

a = MyClass()
print(globals())
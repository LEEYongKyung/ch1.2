#module name: mymod

print('mymodule.py의 모듈이름: '+__name__)

def main():
    print('최상의 모듈(실행모듈, 독립실행)시 출력 합니다. ')

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

if __name__ == '__main__':
    main()
else:
    print('모듈이름: '+__name__)


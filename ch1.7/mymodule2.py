#module name: mymodule2

import mymodule


def main():
    print('독립실행 시, 출력됩니다.')

def power(x,y):
    r =1
    for i in range(y):
        r = mymodule.multiply(r, x)

    return r

if __name__ == '__main__':
    main()
else:
    print('모듈이름:'+__name__)
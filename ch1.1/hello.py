#HELLO
print('Hello world')
a=1
if a >1:
    print(a)
    print('BIG')
    s = 'hello'
    if a+1==2:
        print(1)
        print(2)

print('end')


def int2digit(n, base):
    res = ''
    while n>0:
        n,r = divmod(n,base)
        res = str(r) + res
        print(res)
    return res

result = int2digit(22,2)
print(result)
# if ~ else
a =10
if a >5:
    print('Big')

a = 3
if a >5:
    print('Big')
else:
    print('small')

if a >5:
    print('Big')
else:
    print('small')

n = -2
if n>0:
    print('양수')
elif n<0:
    print('음수')
else:
    print('0')


#
#  spam : 100
#  egg : 500
#  spagetti = 2000

price = 0
goods = 'spam'
if goods == 'spam':
    price = 100
elif goods == 'egg':
    price = 500
elif goods == 'spagetti':
    price = 2000
else:
    price = 0
print(price)


#삼항 연산자
#다른 언어:
#
# message = a > 5 ? 'big' : 'small'
# print(message)

#파이썬:
a = 10
print( 'big' if a>5 else 'small')

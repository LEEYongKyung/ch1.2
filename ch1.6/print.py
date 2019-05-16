#print 함수 연습
import  sys
print((1))
print(('hello','world'))

x = 0.2
s = 'hello world'
# sep , end 파라미터 지정하기
print(x,s,sep=",")
print(str(x) +','+s)


print(x,s,sep=',',end='') #end에 개행을 없엠
print('******')
#기본적인 print()호출은
print(sep=' ', end='\n')

#file 파라미터를 지정 할 수 있다.
print('Hello World', file=sys.stdout) # stdout은 콘솔
print('error: Hello World', file=sys.stderr) #

#file에 출력
f = open('hello.txt', 'w')
print('HELLO WORLD',file=f)


#참고
sys.stdout.write('HELLO WORLD')

#zip()함수 사용 예
seq1 = {'foo','b','c'}
seq2 = {'one','two','three'}

z =  zip(seq1,seq2)
print(z)
print(type(z))
#수회
for t in z:
    print(t, type(t)) #zip은 한번 풀려서 순회하면 다시 사용 불가 , 다시 묶어줘야함

z = zip(seq1, seq2)
for index, t in enumerate(z):
    print(index,t)


z = zip(seq1, seq2)
for index, (a,b) in enumerate(z):
    print(index,(a,b))


d1 = [('foo','one'),('fooo','two'),('fooooo','three')]
seq1, seq2 = zip(*d1) #개별적인 여러개로 보겠다는 듯
print(seq1)
print(seq2)

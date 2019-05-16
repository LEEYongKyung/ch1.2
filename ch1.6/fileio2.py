#다양한 파일 입출력 함수

f= open('text.txt','r',encoding='UTF-8')
text = f.read()
print(text)

pos = f.tell()
print(pos)

# position을 이동 시키고 다시 읽기
f.seek(17)

text = f.read()
print('______'+text+"-----")

f.close()



# 라인단위 읽기
line_num = 0
f2 = open('fileio2.py','rt',encoding='UTF-8')
while True:
    line = f2.readline()
    if line == '':
        f.close()
        break
    line_num += 1
    print('{0}: {1}'.format(line_num,line), end='')


f3 = open('fileio2.py','rt',encoding='UTF-8')
for line_num, line in enumerate(f3.readlines()) :
    print('{0}: {1}'.format(line_num,line), end='')
f3.close()

# with - as 문을 사용하면 자동으로 파일이 닫힌다.
with open('fileio2.py','rt',encoding='UTF-8') as f4:
    for line_num, line in enumerate(f4.readlines()) :
        print('{0}: {1}'.format(line_num,line), end='')

print('\n',f4.closed) # f4가 닫혔는지

# write test

#default mode는 text 모드 이다.
f = open('text.txt', 'w', encoding='UTF-8')
write_size = f.write('안녕하세요\n 둘리입니다.') #g한글은 한 글자당 3바이트
f.close()

print(write_size)


#binary mode :wb
f = open('test2.txt', 'wb')

write_size = f.write(bytes('안녕하세요\n 둘리입니다.', encoding='UTF-8')) #g한글은 한 글자당 3바이트
f.close()
print(write_size)
print(write_size)



#read test
f = open('text.txt','r',encoding='utf-8')
text=f.read()
f.close()
print(text)


#  copy binary file

f_src= open('python.png','rb')
data = f_src.read()
f_src.close()
print(type(data))

f_dst = open('python2.png','wb')
f_dst.write(data)
f_dst.close()
a = 23
print(a, type(a))
print(isinstance(a, int)) #isinstance 해당 객체인지를 검사 맞으면Ture 틀리면 False

#binary, Decimal, Octa, Hex
b = 0b1101 #binary
c = 0o23
d = 0x23


print(b)
print(c)
print(d)

e = 2**1024  # **는 승수

print(e, type(e))
print(e.bit_length) #bit_length 얼마나 많은 비트를 사용하는지

#진법 변환 변환함수
oct(38)#10진수를 8진수 변환
print(oct(38))
print(hex(38))
print(bin(38))

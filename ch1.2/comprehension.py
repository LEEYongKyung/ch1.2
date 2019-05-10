#compre안쓰는 경우
results = []
for num in [1,2,3,4,5,6,7,8]:
    result = num*num
    results.append(result)


print(results)

#comprehension : 간결하게 표현하는것

results = [ num*num for num in [1,2,3,4,5,6,7,8]]
print(results)


#문자열 리스트에서 길이가 2 이하인 문자열 리스트 만들기
strings = ['a','aa','bat','cat','dove']
strings = [s for s in strings if len(s)<=2]
print(strings)

#1~100 t사이의  수 중에서 짝수 리스트 만들기
evens = [i for i in range(1,101) if i%2 == 0]
print(evens)

#[실습] 1~100 사이에 3,6,9사 있는 수 리스트 만들기
results = [ number for number in range(1,101) if str(number).count('3')>0 or str(number).count('6')>0 or str(number).count('9')>0]
print(results)



# 문자열 리스트에서 문자열 길이를 순차 자료형으로 저장해 보자
strings = ['a','aa','bat','cat','dove']
lens = [len(s) for s in strings]
print(lens)

#dict comprehension
strings = ['a','aa','bat','cat','dove']
dicts = {s:len(s) for s in strings}
print(dicts)


# set comprehension
strings = ['a','aa','bat','cat','dove']
strings = {s for s in strings if len(s)<=2}
print(strings)

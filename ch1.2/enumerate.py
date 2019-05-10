#enumerate() 함수 사용

#사용을 안할경우
i=0
for color in ['red','yellow','blue','gray']:
    print(i, color)
    i = i+1

    #enumerate사용
for i, color in enumerate(['red','yellow','blue','gray']):
    print(i, color)
    
#동적 import를 위한 함수 __import__ 함수

import sys
#동적으로 pythonpath 잡기
sys.path.append('../python_modules')
m=__import__('mymath')

print(m.pi)
print(m.add(10,20))
print(m.area_circle(5))
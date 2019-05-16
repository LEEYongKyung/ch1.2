# 다양한 import 방법

#일반
# import math
# print(math.sin(math.pi/6),math.cos(math.pi/6))


# from math import sin, cos, pi
# import sys
# print(sin(pi/6),cos(pi/6))

# from math import sin, cos, pi
# import sys
# sys.path.append('/PythonStudy/02.PyCharmProjects/python_modules/')
#
# print(sys.path)
#
# from mymath import pi
#
# print(sin(pi/6),cos(pi/6))

#
# 많이 사용하는 방법
# import math as m  #module의 이름을 다른 이름으로 변경
# print(m.sin(m.pi/6),m.cos(m.pi/6))


from math import sin as mysin, cos as mycos, pi
import sys
print(mysin(pi/6),mycos(pi/6))
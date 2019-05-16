#모듈 탐색 경로 확인

import sys
sys.path.append('/PythonStudy/02.PyCharmProjects/python_modules/')

print(sys.path)

import mymath

print(mymath.pi)
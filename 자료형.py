##################################################

# 리스트 list

list = ["a", "b", "c"]

list[0]
list.append("d") # 추가
list.insert(2, "a") # 원하는 위치에 추가
list.pop() # 빼기
list.index("a") # 찾기
list.count("a") # 세기

num_list = [5,2,3,4,1]

num_list.sort() # 정렬
num_list.reverse() # 뒤집기
num_list.clear() # 모두 지우기
num_list.extend(list) # 확장

##################################################

# 사전 dict

dict = {1: "a", 2: "b"}

dict[1] # Key 가 없으면 오류
dict.get(1) # Key 가 없으면 None
dict.get(3, "사용 가능") # Key 가 없으면 뒷값 출력
print(1 in dict) # True
dict[1] = "A" # 교체
del dict[2] # 삭제
dict.keys() # Key
dict.values() # Value
dict.items() # Key, Value
dict.clear() # 모두 지우기

##################################################

# 세트 set

low_set = {"a", "b", "c"} # 중복 X 순서 X
up_set = {"A", "B", "C"}

low_set & up_set # 교집합
low_set.intersection(up_set)
low_set | up_set # 합집합
low_set.union(up_set)
low_set - up_set # 차집합
low_set.difference(up_set)
low_set.add("d") # 추가
up_set.remove("C") # 제거

##################################################

# 튜플 tuple

tuple = ("a", "b") # 고정된 값
tuple[0]
(a, b) = ("a", "b")

##################################################

# 불리언 bool

print(True)
print(not True)
print(1 > 0) # 부등식
print(2 >= 1)
print(1 == 1) # 같다
print(1 != 1) # 다르다
print((1 > 0) and (2 > 1)) # 모두 만족
print((1 > 0) & (2 > 1))
print((1 < 0) or (2 > 1)) # 하나라도 만족
print((1 < 0) | (2 > 1))
print(3 > 2 > 1) # 삼단 부등식

##################################################

# 문자열 str

str = "a"
str = "a" * 3
str = """
a
b
c
"""

str = "Be Awesome Today"

str.lower() # 소문자로 변환
str.upper() # 대문자로 변환
str[0].isupper() # 0 번째 문자가 대문자인가?
len(str) # 길이
str.replace("Today", "Tomorrow") # 교체
where = str.index("e") # 찾기, 원하는 값이 없으면 오류
str.index("e", where + 1) # 첫 문자의 위치 이후 문자의 위치
str.find("Today") # 찾기, 원하는 값이 없으면 -1 출력
str.count("e") # 개수

# 슬라이싱
slice = "abcdefg"

slice[0] # 0 번째
slice[0:3] # 0 ~ 3 직전까지
slice[:3] # 처음부터 3 직전까지
slice[3:] # 3 부터 끝까지
slice[-3:] # 뒤에서 3 번째부터 끝까지

# 문자열 포맷
print("12%d4" % 3) # 정수
print("ab%sd" % "c") # 문자열
print("%cBCD" % "A") # 문자
print("drea{}".format("m"))
print("dre{}{}".format("a", "m"))
print("dre{0}{1}".format("a", "m"))
print("dre{x}{y}".format(x = "a", y = "m"))
x = "a"
y = "b"
print(f"{x}{y}solute")

print("{0: >10}".format(500)) # 빈칸 빈공간, 오른쪽 정렬, 총 10 칸 확보
print("{0: >+10}".format(-500)) # +- 부호
print("{0:_<+10}".format(500)) # 왼쪽 정렬, 빈칸 _
print("{0:,}".format(100000000000)) # 3자리 마다 쉼표
print("{0:+,}".format(-100000000000)) # 3자리 마다 쉼표, +- 부호
print("{0:^<+30,}".format(-100000000000)) #  빈칸 ^, 왼쪽 정렬, 총 30 칸 확보, 3자리 마다 쉼표, +- 부호 
print("{0:f}".format(5/3)) # 소수점 출력
print("{0:.2f}".format(5/3)) # 소수점 n 째 자리까지 표시

# 탈출문자
print("a\\b") # 역슬래시
print("a\nb") # 줄바꿈
print("a \"b\" c \'d\' e") # 따옴표
print("Red Apple\rPine") # 커서 맨 앞으로 이동
print("Redd\bApple") # 백스페이스
print("Red\tApple") # 탭

##################################################

# 실수 float 정수 int

float = 3.14
int = 1

num = 1 * 1 # 곱셈
num = 4 / 2 # 나눗셈
num = 3 % 2 # 나머지
num = 3 // 2 # 몫
num = 2 ** 3 # 거듭제곱

num = 1
num += 2 # num = num + 2
num -= 2 # num = num - 2
num *= 4
num /= 2
num %= 3

abs(-1) # 절댓값
pow(2, 3) # 거듭제곱
max(1, 2) # 큰 값
min(1, 0) # 작은 값
round(3.14, 1) # 반올림, 소수점 n 째 자리까지 표시

from math import *

floor(3.14) # 내림
ceil(3.14) # 올림
sqrt(16) # 제곱근

##################################################
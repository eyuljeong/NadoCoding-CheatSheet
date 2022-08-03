##################################################

# 랜덤함수

from random import *

random() # 0.0 ~ 1.0 미만의 임의의 값 생성
int(random() * 10) # 0 ~ 10 미만의 임의의 정수 생성
randrange(1, 10) # 1 ~ 10 미만의 임의의 정수 생성
randint(1, 10) # 1 ~ 10 이하의 임의의 정수 생성

##################################################

# 표준입출력

print("a" + "b", end = " ") 
print("a", "b", sep = " and ")
print("a".ljust(3), "b".rjust(3), sep = ":") # 좌우로 정렬
print("12".zfill(4)) # 총 4 칸 확보, 빈칸 0

import sys
print("a", "b", file = sys.stdout)
print("a", "b", file = sys.stderr)

answer = input("hi ")
print(type(answer))

##################################################

# for

for i in [1,2,3,4,5]:
    print(i)
for i in range(1, 6): # 1 부터 6 직전까지
    print(i)

num = [1,2,3,4,5]
num = [i + 100 for i in num]
alp = ["a", "b", "c"]
alp = [len(a) for a in alp]

# enumerate
lst = ["a", "b", "c"]

for lst_idx, lst_val in enumerate(lst):
    print(lst_idx, lst_val) # 값의 위치, 값

##################################################

# while

index = 1
while index <= 5:
    print("hi")
    index += 1

# 무한루프
# while True:
#     print("hi")

##################################################

# if

answer = input("answer = ")
if answer == "a":
    print(1)
elif answer == "b":
    print(2)
else:
    print(3)

##################################################

# continue & break

num1 = [1, 2]
num2 = [5]

for i in range(1, 10):
    if i in num1:
        continue # 넘어가기
    elif i in num2:
        break # 종료
    print(i)

##################################################

# try

try:
    num1 = float(input("num1 = "))
    num2 = float(input("num2 = "))
    print(num1 / num2)
except ValueError:
    print("type float")
except ZeroDivisionError:
    print("can't divide with 0")
except Exception as err:
    print(err)

 # 에러 발생시키기
try:
    num = float(input("num = "))
    if num > 0:
        raise ValueError
except ValueError:
    print("type 0 or negative num")

# 사용자 정의 에러
class HereWeGoAgain(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self): # err 로 return
        return self.msg

try:
    num = float(input("num = "))
    if num > 0:
        raise HereWeGoAgain("type 0 or negative num")
except HereWeGoAgain as err:
    print(err)

##################################################

# 파일 입출력

text = open("text_file", "w", encoding = "utf8") # 쓰기
print("text", file = text)
text.close()
text = open("text_file", "a", encoding = "utf8") # 추가
text.write("file")
text.close()
text = open("text_file", "r", encoding = "utf8") # 읽기
text.read() # 파일 전체 불러오기
text.readline() # 줄별로 읽기, 한 줄 읽고 커서가 다음 줄로 넘어감

# 파일이 몇줄인지 모를 때
while True:
    line = text.readline()
    if not line: # 줄이 없으면
        break
    print(line, end = "")
    
# 리스트 형태
lines = text.readlines() # 리스트로 저장
for line in lines:
    print(line, end = "")
text.close()

##################################################

# pickle

import pickle

pickle_txt = open("pickle_txt", "wb") # 쓰기
text = "pickle"
pickle.dump(text, pickle_txt) # text 를 pickle_txt 에 저장
pickle_txt.close()
pickle_txt = open("pickle_txt", "rb") # 읽기
text = pickle.load(pickle_txt) # pickle_txt 의 정보를 text 에 불러오기
pickle_txt.close()

##################################################

# with

with open("pickle_txt", "rb") as pickle_txt: # with 로 pickle 읽기
    pickle.load(pickle_txt)
with open("with_txt", "w", encoding = "utf8") as with_txt: # 쓰기
    with_txt.write("with")
with open("with_txt", "r", encoding = "utf8") as with_txt: # 읽기
    with_txt.read()

##################################################
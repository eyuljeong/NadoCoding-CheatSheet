##################################################

# 모듈

import module
module.alpha(1)

import module as md # nickname
md.beta(2)

from module import * # 전체 import
gamma(2)

from module import alpha, beta # 선택적 import
alpha(1)
beta(4)

from module import gamma as c # 선택적 import + 함수 nickname
c(1)

##################################################

# 패키지

import package.alpha
# import package.alpha.A # 불가능
cls = package.alpha.A()
cls.command()

from package import alpha # from 패키지 import 모듈
cls = alpha.A()
cls.command()

from package.beta import B # from 패키지.모듈 import 클래스
cls = B()
cls.command()

from package import * # 공개 범위 설정 : __init__.py
cls = alpha.A()
cls = beta.B()
cls.command()

import inspect # 패키지, 모듈 위치 확인
import random
print(inspect.getfile(random))
print(inspect.getfile(alpha))

##################################################

# 내장함수
# Built-in Functions 참고

answer = input("hi") # 사용자 입력을 받는 함수
import random
print(dir()) # 가지고 있는 변수와 함수 표시
print(dir(random)) # random 함수 상세 정보
list = [1,2,3,4]
print(dir(list)) # 리스트에서 쓸 수 있는 함수

##################################################

# 외장함수
# Python Module Index 참고

import glob # 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
print(glob.glob("*.py")) # 확장자가 py 인 모든 파일

import os # 운영체제에서 제공하는 기본 기능
print(os.getcwd()) # 현재 디렉토리
print(os.listdir()) # 현재 경로 내 폴더 / 파일 목록 조회
folder = "folder"
os.makedirs(folder) # 폴더 생성
os.rmdir(folder) # 폴더 지우기

import time # 시간 관련 함수
print(time.localtime()) # 현재 시간
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 연-달-일 시-분-초

import datetime 
today = datetime.date.today() # 오늘 날짜
td = datetime.timedelta(days = 100) # 100일 저장
print(today + td) # 오늘부터 100일 후

##################################################

# pip

# pip install (패키지) : 다운로드

# pip install --upgrade (패키지) : 패키지 업데이트

# pip uninstall (패키지) : 패키지 삭제

# pip list : 다운로드 된 패키지 리스트

# pip show (패키지) : 패키지 상세정보

##################################################
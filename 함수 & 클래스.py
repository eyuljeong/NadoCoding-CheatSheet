##################################################

# 함수

def adition(num1 , num2):
    print("{0} + {1} = {2}".format(num1, num2, num1 + num2))
    return num1 + num2

add_num = adition(1, 1)
print(add_num)

# 기본값
def adition(num1, num2 = 2):
    print("{0} + {1} = {2}".format(num1, num2, num1 + num2))
    return num1, num2

num1, num2 = adition(1, 1)
print(num1, num2)
num1, num2 = adition(1) # 기본값 반영, num2 = 2
print(num1, num2)

# 키워드값
def number(a, b, c):
    print(a, b, c)

number(b = 1, c = 7, a = 3)

# 가변인자
def string(alpha, beta, *gamma):
    print(alpha, beta, end = " ")
    for r in gamma: # 인자들을 gamma 에 tuple 로 저장
        print(r, end = " ")
string("a", "b", 1, 2, 3, 4)
print("")

# 지역변수, 전역변수
num1 = 1
def multiply(num2):
    global num1 # 전역 공간의 num1 사용 (비추)
    num1 = num1 * num2

multiply(1)
print(num1)

def multiply_ret(int1, int2):
    int1 = int1 * int2
    return int1 # return (추천)

int1 = multiply_ret(1, 2)
print(int1)

##################################################

# 클래스

class Unit:
    def __init__(self, name, hp, dps): # 생성자
        self.name = name # 멤버변수
        self.hp = hp
        self.dps = dps
        print("{0} : hp = {1} | dps = {2}".format(self.name, self.hp, self.dps))
    
    def attack(self): # 메소드
        print("{0} : 적에게 {1} 데미지".format(self.name, self.dps))

moong = Unit("뭉치", 100, 10)
moong.attack()

moong.rage = True # 멤버변수 확장
if moong.rage == True:
    print("월우러월월!!")

# 상속
class Pet(Unit): # Unit 을 상속
    def __init__(self, name, hp, dps):
        Unit.__init__(self, name, hp, dps) # Unit 의 멤버변수를 상속

    def help(self):
        self.attack() # 메소드 오버라이딩, attack 함수 재정의

enyul = Pet("은율", 50, 5)
enyul.help()

# super
class A:
    def __init__(self, a):
        self.a = a
        print(a)

class B:
    def __init__(self, b):
        self.b = b
        print(b)
    

class C(A, B): 
    def __init__(self, a, b):
        super().__init__(a) # super 는 상속된 첫 클래스만 호출, self 쓸 필요 없음
        B.__init__(self, b) # 따라서 뒤에 나오는 B.__init__ 을 호출해줘야함

hi = C("alpha", "beta")

##################################################
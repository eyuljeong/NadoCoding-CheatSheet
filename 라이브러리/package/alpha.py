class A:
    def command(self):
        print("alpha command")
    
if __name__ == "__main__": # 직접 실행
    print("alpha 모듈 직접 실행")
    cls = A()
    cls.command()
else: # 외부 실행
    print("alpha 모듈 외부 실행")
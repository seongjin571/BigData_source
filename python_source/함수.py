class human:
    이름="한성진"
    def say(self):
        print("내 이름은 %s"%self.이름)
class sungjin(human):
    성별="남자"
    def hello(self):
        print("%s성별은 %s입니다."%(self.이름,self.성별))
hu=sungjin()
hu.hello()
5

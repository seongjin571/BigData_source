class calculator:
    result=0.0
    name=''
    def __init__(self,a):
        self.name=a
    def add(self,*plu):
        for i in plu:
            self.result+=i
    def subtract(self,min):
        self.result-=min
    def multiply(self,mul):
        self.result*=mul
    def divide(self,div):
        self.result/=div
cal=calculator("똑똑한계산기")
cal.add(5)
cal.multiply(10)
cal.subtract(2)
cal.divide(3)
print(cal.result)







num=int(input("숫자를 입력하시오 : "))
count=0
for i in range(2,num):
    if num%i==0:
        count=1
if count==1:
    print("False")
else:
    print("True")
  

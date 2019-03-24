import random
num=  random.randint(1,100)
count=0
for i in range(1,11):
    user=int(input("숫자를 맞춰보세요 : "))
    count+=1
    if num==user:
        print("맞추셨습니다. %d만에 정답이네요"%count)
        check=1
        break
    elif num<user:
        print("더 작은 수입니다.")
    else:
        print("더 큰 수입니다.")
if check==0:
    print("숫자 맞추기 게임에서 실패하셨습니다.")
        

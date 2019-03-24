num=input("주민등록 번호를 입력하세요 : ")
num2={'1','2','3','4','5','6','7','8','9','0'}

check=0
for i in num:
    for j in num2:
        if i==j:
            check+=1
            break
if check!=13:
    print("숫자로 입력하세요")
elif len(num)!=13:
    print("13자리로 입력하세요")
else:
    mw=num[6]
    if mw=='1':
        print("남자")
    else:
        print("여자")

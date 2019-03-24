def gugudan(a=2):
    if a>=2 and a<=9:
            for i in range(1,10):
                print(a,"x",i,'=',a*i)
num=int(input("숫자를 입력하세요 : "))
gugudan(num)



        
print("="*30)




def getAvgNum(*a):
    sum=0
    count=0
    average=0
    for i in a:
        sum+=i
        count+=1
    average=sum/count
    print(average)
getAvgNum(32,2,13,53,34)
    



        
print("="*30)




def getMaxNum(*a):
    max=0
    for i in a:
        if i>max:
            max=i
    print(max)
getMaxNum(24,35,64,32,22,3)




print("="*30)



def getfood(a):
    food = { "떡볶이" : "오뎅" ,
             "짜장면" : "단무지",
             "라면" : "김치", 
             "피자" : "피클", 
             "맥주" : "땅콩", 
             "치킨" : "치킨무", 
             "삼겹살" : "상추"     
    }
    count=0
    for i in food:
        if a==i:
            count=1
            print(food[i])
    if count==0:
        print("찾는 자료가 없습니다.")
find=input("찾는 자료를 입력하세요 : ")
getfood(find)






















    

import random
num=  random.randint(1,3)
def play(sel):
    num=  random.randint(1,3)
    game={  1 : "가위", 
        2 : "바위", 
        3 : "보"   }
    if game[num]=="가위":
        print("컴퓨터는 가위")
        if sel=="가위":
            print("비기셨습니다")
        elif sel=="보":
            print("지셨습니다..")
        elif sel=="바위":
            print("이기셨습니다..")
    elif game[num]=="바위":
        print("컴퓨터는 바위")
        if sel=="가위":
            print("지셨습니다.")
        elif sel=="보":
            print("이기셨습니다.")
        elif sel=="바위":
            print("비기셨습니다.")
    else:
        print("컴퓨터는 보")
        if sel=="가위":
            print("이기셨습니다.")
        elif sel=="보":
            print("비기셨습니다.")
        elif sel=="바위":
            print("지셨습니다.")
wow=input("가위,바위,보 중 하나를 입력하세요 : ")
play(wow)
            
        
            
        

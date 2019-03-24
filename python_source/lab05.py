money=int(input("돈을 입력하세요 :"))
bigFive=money//50000
bigOne=(money-bigFive*50000)//10000
smallFive=(money-(bigFive*50000+bigOne*10000))//5000
smallOne=(money-(bigFive*50000+bigOne*10000+smallFive*5000))//1000
print("오만원권", bigFive,"장입니다.")
print("만원권", bigOne,"장입니다.")
print("오천원권", smallFive,"장입니다.")
print("천원", smallOne,"장입니다.")

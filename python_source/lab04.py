data = [ "홍길동", [90, 100],
         "김영희", [100,100] ]
data.insert(0,[90,90])
data.insert(0,"김철수")
del data[5]
data.append("제임스")
data.append([90,90])
print(data.index("김철수"))
print(data.index("홍길동"))
print(data.index("김영희"))



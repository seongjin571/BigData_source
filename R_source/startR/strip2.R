subway<-read.csv("Data/sample1-4ȣ���������°���.csv")
subway<-subway %>% filter(�뼱��ȣ=='line_2')
subway<-subway %>% mutate(������=����+����)
boxplot(subway$������)$stats
subway$������<-ifelse(subway$������>7360363 | subway$������<2027026,NA,subway$������)
subway<- subway %>% filter(!is.na(������)) 
subway
ggplot(data = subway, aes(x = �ð�, y = ������)) + geom_line() 

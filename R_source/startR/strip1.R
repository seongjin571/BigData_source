library(ggplot2)
library(dplyr)
exam<-read.csv("Data/emp.csv")
ggplot(data=exam,aes(x=job,y=sal))+geom_point()
ggplot(data=exam,aes(x=hire_year,y=sal))+geom_point()+
  xlim(2000,2017)
boxplot(exam$sal)$stats
exam$sal<-ifelse(exam$sal>5000 | exam$sal<800,NA,exam$sal)
exam
exam2<-exam %>% group_by(job) %>% summarise(ave=mean(sal,na.rm = T))
table(exam2$job)
table(exam2$ave)
ggplot(data = exam2, aes(x = reorder(job, ave), y = ave)) + geom_col()
ggplot(data=exam, aes(x=job))+geom_bar()

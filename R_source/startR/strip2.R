subway<-read.csv("Data/sample1-4È£¼±½ÂÇÏÂ÷½Â°´¼ö.csv")
subway<-subway %>% filter(³ë¼±¹øÈ£=='line_2')
subway<-subway %>% mutate(½ÂÇÏÂ÷=½ÂÂ÷+ÇÏÂ÷)
boxplot(subway$½ÂÇÏÂ÷)$stats
subway$½ÂÇÏÂ÷<-ifelse(subway$½ÂÇÏÂ÷>7360363 | subway$½ÂÇÏÂ÷<2027026,NA,subway$½ÂÇÏÂ÷)
subway<- subway %>% filter(!is.na(½ÂÇÏÂ÷)) 
subway
ggplot(data = subway, aes(x = ½Ã°£, y = ½ÂÇÏÂ÷)) + geom_line() 

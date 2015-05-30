library(dplyr)

clicks <- read.csv("~/Projetos/RecSys/clicks100.csv")

myfunction <- function(list){
  list[1]
}

clicks$timestamp <- strptime(sapply(strsplit(as.character(clicks$timestamp), "[.]"), myfunction), "%Y-%m-%d %H:%M:%S")
write.csv(clicks, file = "MyData.csv")
# dataImport <- read.csv("data.csv", colClasses = c("factor","factor","Date"))

df2 <- mutate(newclicks100, diffdate = difftime(newclicks100$timestamp, newclicks100$timestamp.1, unit = "secs"))

write(df2, file = "cliksWithTime")


df3 <- mutate(inverseinverseclicksWithTimeWithEnd, diffdate = difftime(inverseinverseclicksWithTimeWithEnd$V7, inverseinverseclicksWithTimeWithEnd$V6, unit = "secs"))
df3$diffdate <- as.numeric(df3$diffdate)
df4 <- mutate(df3, percentualTempo =  round(df3$V10/diffdate, 2))

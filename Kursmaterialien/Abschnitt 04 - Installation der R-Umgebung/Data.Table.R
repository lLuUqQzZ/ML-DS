# install.packages("data.table")
library(data.table)

df <- data.table(Alter = c(20, 21, 22), Groesse = c(1.80, 1.70, 1.75))
print(df$Alter)

print(min(df$Alter))
print(max(df$Alter))
print(mean(df$Alter))

# print(df[, min(Alter)])
# print(df[, max(Alter)])
# print(df[, mean(Alter)])
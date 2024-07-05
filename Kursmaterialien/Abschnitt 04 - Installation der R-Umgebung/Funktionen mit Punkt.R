# install.packages("data.table")
library(data.table)

df <- data.table(Alter = c(20, 21, 22), Groesse = c(1.80, 1.70, 1.75))
# print("Hallo Welt")

print(class(df))

# print.data.table <- function(df) {
#   print("Hallo Welt")
# }

print(df)


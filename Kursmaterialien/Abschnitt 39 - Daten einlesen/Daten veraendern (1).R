# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

# install.packages("data.table")
library(data.table)

df <- fread("classification.csv")
# df$age <- df$age + 5

# df[success == 1, age := age + 5]
# print(df[success == 1, ])

# df[, adult := age >= 18]
df[, `:=`(adult, age >= 18)]
print(df)



# f <- function(a) {
#  print(substitute(a))
#}
#f(Alter := Interesse)

f <- function(a) {
  print(a)
}
f("Hallo Welt")

#### Beispiel 2 ####
f2 <- function(a) {
  print(a)
}
f2()

#### Beispiel 3 ####
f3 <- function(a) {
  print("---")
  print(a)
  print("...")
}
f3()

#### Beispiel 4 ####
f4 <- function(a) {
  print("---")
  if (!missing(a)) {
    print(a)
  }
  print("...")
}
f4(123)

#### Beispiel 5 ####
f5 <- function(a) {
  print(substitute(a))
}
f5(2 + 3)

#### Beispiel 6 ####
f6 <- function(a) {
  print(substitute(a))
}
f6(Alter + Interesse)

#### Beispiel 7 ####

# install.packages("ggplot2")
library(ggplot2)

# install.packages("data.table")
library(data.table)

df <- data.table(Alter = c(20, 21, 22), Groesse = c(1.80, 1.70, 1.75))
print(df)

qplot(Alter, Groesse, data = df)
# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

# Benoetigte Libraries laden
library(ggplot2)
library(scales)
library(stats)
library(data.table)
library(caret)
library(miscTools)

# Daten einlesen 
# Quelle: https://www.kaggle.com/shivam2503/diamonds
diamonds <- fread("diamonds.csv")

train.index <- createDataPartition(diamonds$price, list = FALSE, p = 0.75)
train <- diamonds[train.index, ]
test <- diamonds[-train.index, ]

# Teil 1: Lineare Regression auf Basis der Spalte "carat"
model1 <- lm(price ~ carat, data = train)
test$model1 <- predict(model1, test)
print(rSquared(test$price, test$price - test$model1))

# Teil 2: Lineare Regression auf Basis der Spalten "x", "y" und "z"
model2 <- lm(price ~ x + y + z, data = train)
test$model2 <- predict(model2, test)
print(rSquared(test$price, test$price - test$model2))


# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

library(data.table)
library(ggplot2)
library(caret)

source("helper.R")

data <- fread("classification.csv")
data$success <- as.factor(data$success)

set.seed(42)
train.index <- createDataPartition(data$success, p = 0.75, list = FALSE)
train <- data[train.index, ]
test <- data[-train.index, ]

# e1071: Institut für Statistik und Wahrscheinlichkeitstheorie, TU Wien
# install.packages("e1071")
library(e1071)

model <- svm(success ~ scale(age) + scale(interest), train, kernel = "linear", cost = 1)
print(model)

pred <- predict(model, test)
print(confusionMatrix(table(pred, test$success))$overall["Accuracy"])

g <- plot_classifier(model, train, success ~ age + interest, proba = FALSE)
print(g)

pred.train <- predict(model, train)
print(confusionMatrix(table(pred.train, train$success))$overall["Accuracy"])
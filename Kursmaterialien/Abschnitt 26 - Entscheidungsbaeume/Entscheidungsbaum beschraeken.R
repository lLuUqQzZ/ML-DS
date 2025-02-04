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

# install.packages("rpart")
library(rpart)

model <- rpart(success ~ age + interest, 
               data = train, 
               parms = list(split = "information"), 
               method = "class",
               control = rpart.control(minsplit = 2, xval = 1, cp = 0.01))
print(model)

# install.packages("rpart.plot")
library(rpart.plot)
prp(model, digits = 4)

rpart.plot(model, digits = 4)

g <- plot_classifier(model, train, success ~ age + interest, proba = TRUE)
print(g)

pred <- predict(model, test, type = "class")
print(confusionMatrix(table(pred, test$success))$overall["Accuracy"])

p <- predict(model, test)
print(p)

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
levels(data$success) <- make.names(levels(data$success))

set.seed(42)
train.index <- createDataPartition(data$success, p = 0.75, list = FALSE)
train <- data[train.index, ]
test <- data[-train.index, ]

# Aufgabe:
# 
# Trainiere ein knn-Modell auf den Daten, und ermittle den besten
# Wert für "k". Welches k ist ideal? Passe dazu den Code weiter 
# unten an. 
#
# Verwende dazu die "knn"-Methode (method = "knn"). 

params <- expand.grid(k = c(1, 3, 4, 5, 6, 7, 8, 11, 15, 21, 25))

# install.packages("randomForest")
model <- train(success ~ age + interest, 
               method = "knn", 
               data = train,
               preProcess = c("scale", "center"),
               trControl = trainControl(
                 method = "repeatedcv", 
                 repeats = 10, 
                 classProbs = TRUE),
               tuneGrid = params)

print(model)

pred <- predict(model, test)
print(confusionMatrix(table(pred, test$success))$overall["Accuracy"])


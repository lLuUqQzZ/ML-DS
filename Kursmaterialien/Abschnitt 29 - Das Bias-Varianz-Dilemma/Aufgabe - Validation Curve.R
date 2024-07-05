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

# Aufgabe: Erstelle eine Validation-Curve für einen randomForest, und ermittle
#          so die ideale Groesse für die einzelnen Baeume!
#          Tipp: Rufe dazu die Dokumentation für die randomForest()-Funktion auf,
#                und schaue dir den Parameter "maxnodes" an. 
#
# --------------------------------->
#  [Allgemein] -----> [Spezifisch]

library(randomForest)


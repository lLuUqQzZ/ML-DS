# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

# Benoetigte Libraries laden
library(ggplot2)
library(data.table)

# Daten einlesen 
# Quelle: https://www.kaggle.com/shivam2503/diamonds
diamonds <- fread("diamonds.csv")

print(mean(diamonds$price))
print(median(diamonds$price))

print(summary(diamonds))
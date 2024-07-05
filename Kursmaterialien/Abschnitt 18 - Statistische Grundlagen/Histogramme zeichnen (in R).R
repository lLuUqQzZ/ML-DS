# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

# Benoetigte Libraries laden
library(ggplot2)
library(data.table)

salaries = c(40000, 40000, 41000, 50000, 54000, 70000, 90000)

qplot(salaries, binwidth = 10000)

diamonds <- fread("diamonds.csv")
qplot(diamonds$price, binwidth = 1000)
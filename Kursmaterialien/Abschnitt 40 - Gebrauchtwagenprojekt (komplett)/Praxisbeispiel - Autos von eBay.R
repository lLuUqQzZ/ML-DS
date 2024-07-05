# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

library(ggplot2)
library(caret)
library(R.utils)
library(data.table)

# Originalquelle der Daten: https://www.kaggle.com/orgesleka/used-cars-database
if (!file.exists("autos.csv")) {
  download.file("http://downloads.codingcoursestv.eu/035%20-%20machine%20learning/data/autos.csv.bz2", "autos.csv.bz2")
  bunzip2("autos.csv.bz2", "autos.csv")
}

#  Ziel: Wir möchten ein Modell entwickeln, welches für *gewöhnliche* Autos den Verkaufspreis schätzen kann
# http://opengeodb.org/wiki/PLZ.tab
cars <- fread("autos.csv", encoding = "UTF-8")
cars[, c("dateCrawled", "dateCreated", "nrOfPictures", "lastSeen", "abtest", "postalCode") := NULL]
print(cars)



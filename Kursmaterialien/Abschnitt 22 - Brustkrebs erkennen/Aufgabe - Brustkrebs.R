# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

library(data.table)
library(ggplot2)
library(caret)

source("helper.R")

# Aufgabe: Lese die Datei "cancer.csv" ein, und sage die Spalte "diagnosis" vorher. 
#          Erstelle dazu ein Modell, welches alle Spalten betrachtet!
#          (Die Formel hierzu ist: "diagnosis ~ .").
# 
#          Berechne anschließend die "Accuracy" auf Basis der Test-Daten!
# 
#          Folgende Warnmeldung darfst du ignorieren: 
#              glm.fit: fitted probabilities numerically 0 or 1 occurred 

cancer <- fread("cancer.csv")
cancer$id <- NULL
cancer$diagnosis <- cancer$diagnosis == "M"
print(cancer)

# Noch zu ergänzen:
#   glm(diagnosis ~ ., control = list(maxit = 100))

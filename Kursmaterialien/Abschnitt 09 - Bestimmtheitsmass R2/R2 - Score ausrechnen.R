# Damit setzen wir das Working Directory auf den Ordner dieser Datei
this.dir <- dirname(parent.frame(2)$ofile)
setwd(this.dir)

# Benoetigte Libraries laden
library(ggplot2)
library(scales)
library(stats)
library(data.table)
library(caret)

# Daten einlesen
hotels <- fread("hotels.csv")
print(hotels)

train.index <- createDataPartition(hotels$`Preis in Mio`, p = 0.75, list = FALSE)
train <- hotels[train.index, ]
test <- hotels[-train.index, ]

# Hiermit verringern wir die Faelle, in denen R die Exponentialschreibweise
# verwendet
options(scipen = 100)

# Modell trainieren
model <- lm(`Preis in Mio` ~ Quadratmeter + Gewinn, data = train)
print(model)

test$`Preis in Mio (Vorhersage)` <- predict(model, test)
print(test)

# Bestimmtheitsmass berechnen
print(summary(model))
print(summary(model)$r.squared)

# install.packages("miscTools")
require(miscTools)

print(rSquared(test$`Preis in Mio`, test$`Preis in Mio` - test$`Preis in Mio (Vorhersage)`))
print(rSquared(test$`Preis in Mio`, test$`Preis in Mio (Vorhersage)` - test$`Preis in Mio`))
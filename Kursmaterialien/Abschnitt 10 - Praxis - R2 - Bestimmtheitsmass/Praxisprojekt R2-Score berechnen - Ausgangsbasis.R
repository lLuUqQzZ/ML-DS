# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}


# Benoetigte Libraries laden
library(ggplot2)
library(scales)
library(stats) # Eigentlich nicht benoetigt, wird i.d.R. automatisch geladen
library(data.table)

# Aufgabe: Bezogen auf unsere Auto-Daten, macht es Sinn, dass wir nicht nur den
#          Kilometerstand, sondern auch die Anzahl PS (Spalte: powerPS) in unser
#          Modell einfliessen lassen? 
#          Erstelle dazu 2 Modelle, einmal ein Modell mit der Spalte PS, einmal 
#          ein Modell ohne die Spalte PS, und vergleiche das Bestimmtheitsmass
#          auf Basis der Testdaten. 
#          Hinweis: Nur wenn du das Bestimmtheitsmass auf Basis der Testdaten 
#          vergleichst, bekommst du raus, welches Modell besser schaetzt - 
#          R^2 auf Basis der Trainingsdaten kann teils sehr daneben liegen
#          (schauen wir uns spaeter aber auch noch an warum / wieso).

# Daten einlesen
cars <- fread("autos_prepared.csv")

# Passe ab hier den Code an!

# Modell berechnen
model <- lm(price ~ kilometer, data = cars)
print(model)

# In Grafik einzeichnen
g <- qplot(kilometer, price, data = cars) + 
  geom_smooth(method = "lm", se = FALSE, color = I("red"))
print(g)

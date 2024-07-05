# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

# install.packages("data.table")
library(data.table)

dt <- fread("wohnungspreise.csv")
print(dt)

# Damit koennen wir die Daten visualisieren
# install.packages("ggplot2")
library(ggplot2)

# install.packages("scales")
library(scales)

# Grafik erstellen und konfigurieren
qplot(Quadratmeter, Verkaufspreis, data = dt) + 
  scale_y_continuous(labels = format_format(scientific = FALSE, big.mark = ".", decimal.mark = ","))

library(stats)
model <- lm(Verkaufspreis ~ Quadratmeter, data = dt)
print(model)

# Verkaufspreis = 3143 + Quadratmeter * 5071
# 3143 + 60 * 5071

qplot(Quadratmeter, Verkaufspreis, data = dt) + 
  geom_smooth(method = "lm", se = FALSE, color = I("red")) + 
  scale_y_continuous(labels = format_format(scientific = FALSE, big.mark = ".", decimal.mark = ","))

# 
dt.pred <- data.table(Quadratmeter = c(31, 91))
dt.pred$Verkaufspreis <- predict(model, dt.pred)
print(dt.pred)

v <- c(30, 120000, 1)
names(v) <- c("Quadratmeter", "Preis", "Anzahl Zimmer")

print(v[1])
print(v["Quadratmeter"])


print(v[c("Quadratmeter", "Preis")])

print(v[1])

print(names(v))
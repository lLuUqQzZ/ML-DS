a <- c(4, 5)
print(a)

b <- 1:5
print(b)

c <- seq(1, 10, 2)
print(c)

d <- c(1, 2, 3)
print(d * 2)

e <- c(1, 2, "Hallo Welt")
print(e)
# print(e * 2)

f <- c(6, 7, 8, 9, 10)
print(f[1])

g <- c(1, 2)
print(f[g])
print(f[c(3, 4, 3)])

# Zugriff über die Index-Schreibweise
success = c(0, 1, 1, 1, 0, 1, 0)
h <- c("nicht bestanden", "bestanden")
print(h[success + 1])

# Zugriff über TRUE/FALSE-Werte
entries <- c(1, 2, 3)
print(entries[c(TRUE, TRUE, FALSE)])
print(entries[c(TRUE, FALSE)])


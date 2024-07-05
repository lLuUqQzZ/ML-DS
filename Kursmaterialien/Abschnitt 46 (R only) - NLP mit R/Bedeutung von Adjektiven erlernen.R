# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

# Sicherstellen, dass alle Pakete korrekt geladen werden, etc. 
source("Installation.R", echo = FALSE)

######################################################################

library(data.table)
library(RDRPOSTagger)
library(caret)

reviews <- fread("Reviews_10000.csv", encoding = "UTF-8")
tagger <- rdr_model(language = "English", annotation = "POS")

pb <- txtProgressBar(min = 0, max = nrow(reviews))

# adj <- sapply(reviews$Text, function(text) {
#   pb.value <- getTxtProgressBar(pb) + 1
#   setTxtProgressBar(pb, pb.value)
#   # print(paste(pb.value, text, sep = ": "))
#
#   res <- tryCatch({
#     tagged <- rdr_pos(tagger, text)
#     paste(tagged[tagged$pos == "JJ", "token"], collapse = " ")
#   }, error = function(err) {
#     return("")
#   })
#   return(res)
# })
# close(pb)
# # Der compress-Parameter sorgt dafür, dass die Daten mit bzip2
# # komprimiert werden, damit sparen wir ca. 500kb ;) 
# saveRDS(adj, "Reviews_10000_adj.rds", compress = "bzip2")

adj <- readRDS("Reviews_10000_adj.rds")
print(adj)
print(adj)


library(readxl)


datos <- read.table(file = "C:/Users/Aleph_0/Coding/UiE/University/2/BasesDatos/Clase03/etanol.txt", header=TRUE)

#Exportación de datos
tipo <- c("A", "B", "C")
longitud <- c(120.34, 99.45, 115.67)
datos <- data.frame(tipo, longitud)
write.table(datos, file = "misdatos.txt")
write.csv2(datos, file = "misdatos.csv")


library(RSQLite)
library(DBI)

db<-RSQLite::datasetsDb()
dbListTables(db)

dbReadTable(db, "CO2")
dbGetQuery(db, "SELECT * FROM CO2 WHERE conc < 100")
dbGetQuery(db, "SELECT type, conc FROM CO2 WHERE conc < 300")
dbGetQuery(db, "SELECT * FROM CO2 ORDER BY Plant")
dbGetQuery(db, "SELECT Plant, Treatment, conc FROM CO2 WHERE Treatment = 'nonchilled' ORDER BY plant desc")

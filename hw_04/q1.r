library("factoextra")
library(cluster)
library(tidyverse)

wine <- read.table("~/Documents/CSI5810/hw_04/wine.data",sep = ",")

wine <- na.omit(wine)

true_label<- wine$V1
#head(wine)
#plot(wine$V4, wine$V5)
k2 <- kmeans(wine, centers = 2, nstart = 25)
k3 <- kmeans(wine, centers = 3, nstart = 25)
k4 <- kmeans(wine, centers = 4, nstart = 25)
k5 <- kmeans(wine, centers = 5, nstart = 25)

p2 <- fviz_cluster(k2,geom = "point", data = wine) + ggtitle("K=2")
p3 <- fviz_cluster(k3,geom = "point", data = wine) + ggtitle("K=3")
p4 <- fviz_cluster(k4,geom = "point", data = wine) + ggtitle("K=4")
p5 <- fviz_cluster(k5,geom = "point", data = wine) + ggtitle("K=5")

library(gridExtra)
grid.arrange(p4,p5, nrow = 2)


library(fossil)
#rand.index(true_label, k2$cluster)

#k2$tot.withinss
vals<- matrix ( c(k2$tot.withinss, k3$tot.withinss,k4$tot.withinss,k5$tot.withinss), ncol=4, byrow=TRUE)
colnames(vals) <- c("K2","K3","K4","K5")
vals <- as.table(vals)
vals
#vals<- matrix ( c(rand.index(true_label,k2$cluster), rand.index(true_label, k3$cluster),rand.index(true_label,k4$cluster),rand.index(true_label,k5$cluster)), ncol=4, byrow=TRUE)
#colnames(vals) <- c("K2","K3","K4","K5")
#vals <- as.table(vals)
#vals

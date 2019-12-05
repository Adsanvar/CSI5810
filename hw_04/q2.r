library(readxl)
library(ggplot2)
CrimeRate <- read_excel("Documents/CSI5810/hw_04/CrimeRate.xlsx")

x1 = CrimeRate$X1
vars = as.matrix(CrimeRate[,3:7])
data <- data.frame(vars, x1)
#To find the minimal error (least sqaure)
cost <- function(X, y, theta)
{
  sum( (X %*% theta - y)^2 ) / (2*length(y))
}

delta <- function(x, y, theta) {
  error <- (x %*% theta - y)
  delta <- t(x) %*% error/length(y)
  return((delta))
}

# gradient descent algo
gradescent <- function(x, y, theta, alpha) {
  theta <- theta - alpha * delta(x, y, theta)
  return(theta)
}

lm1 <- lm(x1 ~ CrimeRate$X3 + CrimeRate$X4 + CrimeRate$X5 + CrimeRate$X6 + CrimeRate$X7)
summary(lm1)
#least sqaures parameter estiamtes
theta_lm <-coef(lm1) 
print(theta_lm)
#Residuals
#res = target - predict(lm1)
#print(lm1$residuals)

#R^2 coefficient of regression
summary(lm1)$r.squared

#SSR - sum of sqaured residuals
mean(residuals(lm1)^2)
#plot( lm1$residuals ~seq(1, 50, by=1), main="Crime Rate Risiduals")
#print(ggplot(data ,aes(seq(1, 50, by=1), target)) +geom_point()+geom_abline( intercept = theta_lm [1] , slope = theta_lm [2] , size =2 , color =I( "red ")))
#layout(matrix(c(1,2,3,4), 2, 2))
#plot(lm1) 

x3 = CrimeRate$X3

alpha <- 0.01
epochs <- 1000
cost_history <- double(epochs)
theta_history <- list(epochs)

theta <- matrix(c(0,0), nrow = 2)

Xp <- cbind(1, x3)

for (i in 1:epochs)
{
  error <- (Xp %*% theta - x1)
  delta <- t(Xp) %*% error / length(x1)
  theta <- theta - alpha * delta
  cost_history[i] <- cost(Xp, x1, theta)
  theta_history[[i]] <- theta
  
}

print(theta)



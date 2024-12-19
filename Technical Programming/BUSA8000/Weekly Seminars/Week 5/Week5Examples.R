# Week 5 Examples 

# Example 1: Suppose the heights of individuals in a sample of 5 observations are given by:
# { 1.8, 1.72, 1.78, 1.7, 1.6 }
# The observations are in terms of meters.
# Assume that before sampling the heights are independent and identically distributed
# with the common distribution N(mu, sigma^2), where sigma^2 = 0.25
# Test the null hypothesis H_0: mu = 1.75 
# against the alternative hypothesis H_1: mu is not equal to 1.75
# at significance level 5%

x <- c(1.8, 1.72, 1.78, 1.7, 1.6)
sigma <- sqrt(0.25)
xbar <- mean(x)
t <- (xbar - 1.75) / (sigma / sqrt(5))
pvalue <- 2 * (1 - pnorm(abs(t), 0, 1))
pvalue 

#> pvalue
#[1] 0.8932728
# Since pvalue is much greater than 5%,
# we do not reject H_0 at 5% significance level.

#Example 2: Consider the data in Example 1. 
#Construct a 95% confidence interval for the 
#unknown mean mu.

z <- qnorm(0.975, 0, 1) 
LL <- xbar - z * sigma / sqrt(5)
UL <- xbar + z * sigma / sqrt(5)
LL
#> LL
#[1] 1.281739

UL
#> UL
#[1] 2.158261




  
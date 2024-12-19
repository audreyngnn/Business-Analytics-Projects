# Week 5 Examples 

# Example 1: Suppose the heights of individuals in a sample of 5 observations are given by:
# { 1.8, 1.72, 1.78, 1.7, 1.6 }
# The observations are in terms of meters.
# Assume that before sampling the heights are independent and identically distributed
# with the common distribution N(mu, sigma^2), where sigma^2 = 0.25

'''
In the context of a normal distribution N(mu, sigma)
The standard deviation is a measure of a measure of the amount of variation or dispersion in a set of values.
when squared represents the variance of the distribution,
which is the average if the squared differences form the mean.
So, in short, sigma is the standard deviation, and sigma^2 is the variance

'''

# Test the null hypothesis H_0: mu = 1.75 
# against the alternative hypothesis H_1: mu is not equal to 1.75
# at significance level 5%

x <- c(1.8, 1.72, 1.78, 1.7, 1.6)
sigma <- sqrt(0.25) #Compute the sample mean
xbar <- mean(x) #Compute the test statistic 
t <- (xbar - 1.75) / (sigma / sqrt(5)) #Compute the p-value
# the t-statistic: figure out if the difference between two sets of data is real
# or just due to random chance.
# t = (x-mu)/(sigma/sqrt(n))

# If the t-statistic is big, it means the difference between the groups is probably real
# and not just random chance.
# But if it's small, the diffrence might just be luck.

pvalue <- 2 * (1 - pnorm(abs(t), 0, 1)) #2 mean two sided test
pvalue 

# 1 - pnorm(abs(t), 0, 1): Probability of obtaining a value greater than the abs value of t
# in a standrad normal distribution.

pvalue

#> pvalue
#[1] 0.8932728
# Since the p-value is much greater than 5%,
# we do not reject H0 at 5% significance level.

# There is 89% chance of making an error when you reject H0



#Example 2: Consider the data in Example 1. 
#Construct a 95% confidence interval for the unknown mean mu.

#Compute the critical value at 5% significance level
#for a two-sided test
z <- qnorm(0.975, 0, 1) #Compute the lower limit of the C.I.
# what value (x-score) corresponds to a given probability under the stanard normal
# distribution.
#0.975 is the probability value

'''In a two-tailed hypothesis test or a two-sided confidence interval,
we are interested in capturing a certain proportion of the probability mass under the curve
of a standard normal distribution. When we talk about a 95% confidence interval or
a significance level of 0.05 in hypothesis testing, we are essentially saying that we want to
capture 95% of the probabl=ility mass under the curve, leaving 2.5% in each tail of the distribution'''

# In this case, it represents the area under the standard normal curve to the left of the z-score.
LL <- xbar - z * sigma / sqrt(5) #Compute the lower level of the CI
UL <- xbar + z * sigma / sqrt(5) #Compute the upper level of the CI

LL
#> LL
#[1] 1.281739

UL
#> UL
#[1] 2.158261



# Example 3: Suppose the heights of individuals in a sample of observations are given by:
# {1.8, 1.72, 1.78, 1.7, 1.6, 1.61, 1.77, 1.69, 1.82}
# The observations are in terms of meters.
# Assume that before sampling the heights are independent and identically distributed
# with the common distribution N(mu, sigma^2).
# Test the null hypothesis H_0: mu = 1.75 
# against the alternative hypothesis H_1: mu is not equal to 1.75
# at significance level 5%

y <- c(1.8, 1.72, 1.78, 1.7, 1.6, 1.61, 1.77, 1.69, 1.82)
# Compute the sample standard deviation as an estimate of
# the unknown population standard deviation 
sy <- sd(y)
ybar <- mean(y)
# Compute the number of observations in the sample 
ny <- length(y) 
t <- (ybar - 1.75) / (sy / sqrt(ny))
df <- ny-1
# "lower.tail = TRUE" by defaultpva
pvalue <- 2 * (1 - pt(abs(t), df, lower.tail = TRUE)) 
pvalue

#> pvalue
#[1] 0.3061684
# Since the p-value is much greater than 5%,
# we do not reject H_0 at 5% significance level. 

#Example 4: Consider the data in Example 3. 
#Construct a 99% confidence interval for the 
#unknown mean mu. 

#Compute the critical value at 1% significance level
#for a two-sided test
tc <- qt(0.995, df, lower.tail = TRUE)
#Compute the lower limit of the C.I.
LL <- ybar - tc * sy / sqrt(ny)
#Compute the upper limit of the C.I.
UL <- ybar + tc * sy / sqrt(ny)
LL
#> LL
#[1] 1.632434

UL
#> UL
#[1] 1.809788


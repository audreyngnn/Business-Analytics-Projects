# In this tutorial (Week 2), a brief introduction to R is provided.
# The content of this tutorial is based on the following reference.
# Reference: Kate Dodds (2021), Macquarie R Users Group - An Introduction to R, 
# https://github.com/mqRusers/2021_03_R-Introduction

# Some links which are useful to download and install R:
# Download R: 
# 1. Windows: https://cran.r-project.org/bin/windows/base/R-3.6.0-win.exe
# 2. Another OS: https://www.r-project.org/
# Download R Studio for Windows and another OS: 
# https://www.rstudio.com/products/rstudio/download/

#### Contents ####

#  1. R for statistical computing 
#  2. R Studio Interface
#  3. Basic commands

#### 1. R for statistical computing ####

###### (i) What is R? ####
#
#  "R is a free software environment for statistical computing and graphics.
#   It compiles and runs on a wide variety of UNIX platforms, Windows and
#   MacOS." (CRAN)
#
#  "In its broadest definition, R is a computer language allowing the user
#   to program algorithms and use tools that have been programmed by others."
#   (Zuur et al 2009 - A Beginner s Guide to R:14)

###### (ii) What might we do using R? ####
#
#  * Manipulate data
#  * Conduct a variety of statistical analyses and computing
#  * Import packages to perform specialised statistical and computing tasks
#  * Design graphics to visualize data 
#  * R as a calculator

###### (iii) Good things of using R ####
#
#  * Free and open-source
#  * A large user base and Massive community for online support 
#    (e.g. online courses, videos and texts)
#  * Contributions from many programmers around the globe
#  * Specific tasks can be mostly computed using packages

#### 2. R Studio Interface ####

#  * R studio provides a user friendly interface 
#    and makes it easier to code in R.
#  * It provides functions simplifying the process of developing code 
#    (e.g. Tab completion and error notifications).

#  What are in R Studio Interface?
#  * 1. Code Editor / R-Script: write and save code here, 
#       just like in a text document
#  * 2. R Console: run code and view the results of the code here
#  * 3. Workspace and History:
#     3.1 Environment: all the loaded data and objects are listed; 
#         Data tables and the structure of the data can be viewed.
#     3.2 History: display the history of executed code
#  * 4. Plots and Files
#     4.1 Files: display the files in the source folder
#     4.2 Plots: show the plots; plots can also be exported from here, 
#         but there may be better ways.
#     4.3 Packages: load and search for new packages; 
#         installed packages are listed here.
#     4.4  Help: look for help or specific vignettes (support documents) 
#          for each package; also access via "?function"
#     4.5 Viewer: can be used to view local web content for web graphics 
#         generated using packages like googleVis, htmlwidgets, and rCharts

#### 3. Basic commands ####

###### (i) Some basic R syntax ####
#
#  * Assignment operator (<-) in R
#  * Assign the value 3 to the object x
#  * Execute the code using Run or Ctrl+Enter
x <- 3
x  # print the object x to see what it contains
#  * This is the same as:
x = 3
x  # print the object x to see what it contains
X  # print the object X to see what it contains
#  Please note that R is case-sensitive.
#  * Assign the sum 2 + 6 to the object y
y <- 2 + 6 # R works like a calculator here and computes the sum
y  # print the object y
y1 <- 2 * (1 + 3) # sum and multiplication
y1 # print the object y1
y2 <- (10 + 6) / 8 # sum and division
y2 # print the object y2 
#
#   * Use the function c() to combine specific values into a vector
#     and assign the vector to the object v
v <- c(2, 4, 6, 8)
v  # print the object v
v1 <- c(1, 2, 3)
v2 <- c(2, 3, 4) 
vsum <- v1 + v2 
vsum # print the object vsum 
v3 <- c(1, 2)
vsum1 <- v2 + v3
#   Why it does not work?
#   check to see what vsum1 is now
#   The objects v2 and v3 are not of the same length
#   so it loops through v3 to give you the 1 again i.e c(1,2,1)+v2
c(1,2,1)+v2
#   * A vector is a sequence of values which could be numbers or letters.

w <- c("a", "b", "c")
w  # print the object w
w1 <- c("Hello!", "How are you?")
w1 # print the object w1

# can we put the different types of elements together
t <- c("hello", 1,3)

## what is the differnce, the numbers are no longer numeric. 
#R will use the most general format.. as you cant change the text to numeric

###### (ii) Functions and arguments ####
#  * Functions are sets of instructions used to do something to arguments.
#  * Arguments are used to tell functions what "objects" to act on 
#  * In mathematics, y = f(x), where f is a function, x is the argument 
#    of f and y is the output of f.
#  * Specify a function called funct with the argument called arg 
#    and assign the output of the function to the object o:
#    o <- funct(arg)
#  * A function with more than one arguments: 
#    function(argument1, argument2,...)
#  * Objects can be used as arguments.
#
v <- c(2, 4, 6, 8)
#  * c() is a function that combines values 2, 4, 6, 8 into the vector 
#    (object) v. The numbers 2, 4, 6, 8 are arguments.

### check to see how long the vector is, as you may have hundreds
length(v)

#
#  * Packages are pre-coded sets of instructions (functions) 
#    that were written by developers or programmers and 
#    are available for everyone to use freely.

###### (iii) More (built-in) functions ####
#  * Use the function mean() to extract the mean of the vector 
#    (object) v and assign the output to (or save it as) a new object m 
#    for later use
m <- mean(v)
m  # print the new object m
#
#  * Use the function median() to extract the median of the vector 
#    (object) v and save it as a new object med
med <- median(v)
med # print the new object med
#
#  * Use the function min() to extract the minimum value of the 
#   (object) v and save it as a new object v_min
v_min <- min(v)
v_min # print the new object v_min
# 
#  * Use the function max() to extract the maximum value of the 
#   (object) v and save it as a new object v_max
v_max <- max(v)
v_max # print the new object v_max
# 
#  * Use of some built-in functions to perform some calculations
u <- cos(1.5) + sin(2.5)
u  # print the object u
u1 <- exp(1)
u1 # print the object u1
u2 <- log(u1)
u2 # print the object u2
#  The function log() gives the natural logarithm with base e
#  e is approximately 2.718281828459 
#  https://en.wikipedia.org/wiki/Natural_logarithm
#
#  * Use the structure function str() to find out more about objects
str(x)
str(y)
str(v)
str(w)
#  
#  * Use the function seq() to create a sequence of values 
s1 <- seq(from = 1, to = 10, by = 1)
s2 <- seq(from = 1, to = 20, by = 2)
s1  # print s1 which contains a vector with the components 1 to 10
    # with an increment of 1
s2  # print s2 which contains a vector with the components 1 to 20
    # with an increment of 2
s1 <- seq(1, 10, by = 1) # if we know the positions of the arguments
s2 <- seq(1, 20, 2) # if we know the positions of the arguments
? seq # look for help and see what is seq and what might it do? 
#
#   * Use the function length() to check the length of an object
length(s1)
length(s2)
#
#   * Use the function cbind() you to combine vectors/columns 
#     to create a "matrix" (a kind of table or array)
#   * The arguments in cbind() must have the same length;
#     otherwise, an error message will result.
s <- cbind(s1, s2)
s  # print the object s which contains a (10 X 2)-matrix 
? cbind # look for help
#   * cbind is for binding "columns"; rbind is for binding "rows".
#   * Use the function rbind() to combine s1 and s2
#     and save it as a new object sr
sr <- rbind(s1, s2)
sr  # print the new object sr
#
#   * Use the function array() to define an array of specific
#     dimension
ar <- array(c(1, 2, 3, 4), dim = c(2, 2))
ar # print the object ar

#check the array to see how many rows and columns.
dim(ar)

ar1 <- array(c(1, 2, 3, 4), dim = c(4, 1))
ar1 # print the object ar1
# 
#   * Use of the function class() to find out the class 
#     to which an object belongs;
#     Say if the object is a vector, a matrix or a dataframe
class(s1)
class(s2)
class(s)


#
#   * Use the plot() function to create a plot
plot(s) # A basic scatterplot of the two columns in the object s
#   * The plot can be modified by adding labeling axis, 
#     changing tickmarks and intervals, adding text or shapes.
#   * A nice plot can be created with just a few lines of code.
#   * Once a plot is coded, it can be re-used and easily modified.
#     This can be useful for research reproducibility. 

#Error in plot.new() : figure margins too large. Why?
#a problem with the margin figure size, width, 
#and height default settings when plotting data 
#in R or R Studio Interface
#a way to fix it is to add par(mar=c(1, 1, 1, 1))
#https://www.programmingr.com/r-error-messages/r-figure-margins-too-large/

par(mar=c(2, 2, 1, 1))
plot(s)

? plot # show the general details about the function plot()
? par # show the graphical parameters / details which can be edited

###### (iv) Import data into R ####
#
#  * If a dataset is built in R, load it by the function data().
data(iris) # load the built-in dataset "iris" using data()
#

## to view the data you can jsut type in

iris

## or 
## to get a better view you ca ntype in

View(iris)

#  * If a dataset is stored in a csv file, 
#    use the function read.csv to import it.
#  * Place the .R file containing the R scripts in the same folder 
#    as the csv file of the dataset "irisdata.csv"
irisdata <- read.csv("irisdata.csv") 



## you can view your current working directory
getwd()

#  Import the dataset and save it as the object irisdata
# * Use of the function summary() to compute some summary statistics
#   of the dataset
summary(irisdata)
# Why the some summary statistics for the variable "Species"
# are not computed?
# Please note that "Species" takes "character" values.
#
# * Consider another dataset "BTC-AUD.csv" and place it in the same folder 
#   as before 
# * Source: Yahoo Finance 
#   https://au.finance.yahoo.com/quote/BTC-AUD/history?p=BTC-AUD
BA <- read.csv("BTC-AUD.csv")
#  Import the dataset and save it as the object BA
# * Use of the function summary() to compute some summary statistics
#   of the dataset
summary(BA)
# Why the summary statistics for all the variables are not 
# computed?
str(BA)
# The data type of each variable in "BTC-AUD.csv" is "character".

#Change the type of the high coulun to double
BA$Hight <- as.double(BA$High)
summary(BA)


#####  (v) Save an object ####
#  * If we make any changes to the dataset, 
#    we can save the new dataset in a .csv file.
#
write.csv(irisdata,  file = "New_irisdata.csv", row.names = FALSE) 
#  * Why "row.names=FALSE" is used?
write.csv(irisdata,  file = "New_irisdata_incl_rownames.csv")

# This is the end of Tutorial.


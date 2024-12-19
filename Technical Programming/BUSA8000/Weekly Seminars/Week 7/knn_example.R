#### Week 7 Lecture (Example 1) ####

library(tidyverse)
library(class)  #this package contains the knn algorithm, and classification functions

knn_data=read_csv(file="wk7_data.csv") 
#load data into R

#inspect data
head(knn_data) 
#inspect the first few entries
#the factors "Factor 1" and "Factor 2"
#will be used for the classification.
str(knn_data) 
#get some basic information about our data
summary(knn_data) 
#calculate some summary statistics about our data
#only useful for numerical values, 
#but not characters

#Plot data
#Let's start by making a plot of the data 
#using the gglot2 package.

ggplot(knn_data) + 
  #load the complete data to be plotted
  geom_point(aes(x=knn_data$Factor_1,y=knn_data$Factor_2,
                 color=knn_data$Classification)) + 
  #create a scatterplot with x-axis being Factor 1
  #and y-axis being Factor 2, and colour by "Classification"
  xlab("Factor 1") +
  #label the x-axis
  ylab("Factor 2") +
  #label the y-axis
  ggtitle("Plot of knn data") +
  #give a title of the plot
  labs(color="Classification") 
  #name the label of the legend by the unique 
  #elements of "Classification"
  #note that for "color", the American spelling
  #is used. 


#from the scatterplot, 
#(1)A, B, and C are colored red, green and blue.
#(2)note that the default colors in your computer
#may be different.
#(3)there are some missing values or NAs in the
#"Classification" column, which have shown up
#in grey.
#(4)the classifications for some of those missing values 
#are obvious. Whereas, some may not have a clear-cut
#answer. 

#note that for this particular data set, it was designed
#to be very obvious. 
#In practice, the different classifications could have 
#large overlaps, and there is no clear correct answer.

#In what follows, the knn algorithm will be used to 
#estimate those missing values or NAs.

#Before running the knn algorithm, some preparation work
#needs to be done. Specifically, we need to set up 
#the following data:
#(1)Training data: the set of points (inputs) for which 
#the classification is known, 
#(e.g., those points without NAs 
#in the classification column)
#(2)Label data: the set of known answers (outputs),
#(e.g, the non-empty entries in the 
#classification column)
#(3)Test data: the set of points (inputs) 
#without classification, (e.g., those points with NAs 
#in the classification column)

#In this unit, we shall not go into the reasoning 
#behind these names.


#create the training data
knn_train_data=na.omit(knn_data) 
#removes any rows containing NA
#use this wisely by first checking 
#no NAs in other columns, say 
#Factor 1 and Factor 2

head(knn_train_data)
#inspect the first few entries of knn_train_data

#create the *label data* by the "Classifications"
#with known answers, (non-empty entries)
#from the training data
knn_labels=knn_train_data %>% 
  select(Classification)
#extract just the classification column

head(knn_labels)
#inspect the first few entries of knn_labels


knn_train_data=knn_train_data %>% 
  select(-ID,-Classification)
#drop the unnecessary columns, say columns 1 and 4, ID and Classification
#classification is our label and ID has no use for us

head(knn_train_data)
#inspect the first few entries of knn_train_data again 

#create the test data 
knn_test_data=knn_data %>%
  filter(is.na(Classification))
#retrieve the unclassified data

head(knn_test_data) 
#view the test data

knn_test_data=knn_test_data %>%
  select(-ID,-Classification) 
#drop the unnecessary columns, say columns 1 and 4

head(knn_test_data) 
#view the test data again

#Use the knn function in the class package 
#to run the knn algorithm,
#and choose k = 5 for this particular data
knn_output=knn(knn_train_data,knn_test_data,knn_labels,k=5) 
#this won't work. Why?
#because knn_labels is a tibble when it was created
#by the select function. 
#we have to convert knn_labels to characters first.

knn_labels_vector = knn_labels$Classification 
#need to do a quick conversion first using the $ sign 

knn_output=knn(knn_train_data,knn_test_data,
               knn_labels_vector,k=5)
#run the knn algorithm with k = 5 again
#this now works. 

knn_output 
#see what the algorithm has produced
#this does not give much information

#plot these outputs
ggplot() +
#we do not specify the argument in the ggplot function
#since we shall use the three data sets here.
  geom_point(data=knn_test_data,
             aes(x=Factor_1, y=Factor_2,
                 color=knn_output)) + 
  #plot the output from the knn algorithm
  geom_point(data=knn_train_data, 
             aes(x=Factor_1, 
                 y=Factor_2,
                 color=knn_labels_vector), 
             alpha=0.1) +
  #plot the original data before applying
  #the knn algorithm 
  #the option alpha is to specify the opacity (or darkness)
  #the display of the data coming with the classification
  #is very light, while the display of the newly classified
  #data is darker.
  #add the things below to make the plot nicer 
  xlab("Factor 1") +
  ylab("Factor 2") +
  ggtitle("Plot of knn data") +
  labs(color="Classification")

#Before saving the original data and the new data
#as a single csv file, we reassemble our data first.

original_data = bind_cols(knn_train_data,knn_labels) 
#put the training data and labels back together
new_data = bind_cols(knn_test_data,data.frame(knn_output))
#put the test data and the output from the knn algorithm
#together

head(original_data) # train data
#check the original data
head(new_data) # test data
#check the new data with the output from knn 

#rename the third column and change to characters
new_data = new_data %>%
  rename(Classification = knn_output) 
  #rename column
new_data$Classification = 
  as.character(new_data$Classification) 
#change to characters

head(new_data) 
#check the new data again

fitted_data = bind_rows(original_data,new_data) 
#glue everything back together, add the train + test together by rows

head(fitted_data) 
#final check

write_csv(fitted_data,"knn_fitted_data.csv") # now we have no na in our final data set

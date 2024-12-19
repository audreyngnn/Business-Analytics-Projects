## https://learn.microsoft.com/en-us/sql/machine-learning/tutorials/r-predictive-model-introduction?view=sql-server-ver16
#Imagine you own a ski rental business and you want to predict the number of rentals 
#that you'll have on a future date. This information will help you get your stock, 
#staff, and facilities ready.



library(rpart);

 
#import data
rentaldata <- read.csv("dbo.rental_data.csv")

#Take a look at the structure of the data and the top rows
head(rentaldata)
str(rentaldata)


#Prepare the data
#In this sample, most of the preparation has already been done, 
#but you'll do one more preparation here. 
#Use the following R script to identify three columns as categories 
#by changing the data types to factor.


#Changing the three factor columns to factor types
rentaldata$Holiday <- factor(rentaldata$Holiday);
rentaldata$Snow    <- factor(rentaldata$Snow);
rentaldata$WeekDay <- factor(rentaldata$WeekDay);


#Visualize the dataset after the change
str(rentaldata);


# The data is now prepared for training.
# To find the best model for the ski rental data, create two different models 
# (linear regression and decision tree) and see which one is predicting more accurately. 
# You'll use the data frame rentaldata that you created.
#

#First, split the dataset into two different sets:
# one for training the model and the other for validating it
train_data = rentaldata[rentaldata$Year < 2015,];
test_data  = rentaldata[rentaldata$Year == 2015,];

#Use the RentalCount column to check the quality of the prediction against actual values
actual_counts <- test_data$RentalCount;

#Model 1: Use lm to create a linear regression model, trained with the training data set
model_lm <- lm(RentalCount ~  Month + Day + WeekDay + Snow + Holiday, data = train_data);

#Model 2: Use rpart to create a decision tree model, trained with the training data set
model_rpart  <- rpart(RentalCount ~ Month + Day + WeekDay + Snow + Holiday, data = train_data);


# Make predictions from both models

#Use both models to make predictions using the test data set.
predict_lm <- predict(model_lm, test_data)
predict_lm <- data.frame(RentalCount_Pred = predict_lm, RentalCount = test_data$RentalCount, 
                         Year = test_data$Year, Month = test_data$Month,
                         Day = test_data$Day, Weekday = test_data$WeekDay,
                         Snow = test_data$Snow, Holiday = test_data$Holiday)

predict_rpart  <- predict(model_rpart,  test_data)
predict_rpart <- data.frame(RentalCount_Pred = predict_rpart, RentalCount = test_data$RentalCount, 
                            Year = test_data$Year, Month = test_data$Month,
                            Day = test_data$Day, Weekday = test_data$WeekDay,
                            Snow = test_data$Snow, Holiday = test_data$Holiday)

#To verify it worked, look at the top rows of the two prediction data sets.
head(predict_lm);
head(predict_rpart);

#Compare the results
#Now you want to see which of the models gives the best predictions. 
#A quick and easy way to do this is to use a basic plotting function to view the difference 
#between the actual values in your training data and the predicted values.


#Use the plotting functionality in R to visualize the results from the predictions
par(mfrow = c(1, 1));
plot(predict_lm$RentalCount_Pred - predict_lm$RentalCount, main = "Difference between actual and predicted. lm")
plot(predict_rpart$RentalCount_Pred  - predict_rpart$RentalCount,  main = "Difference between actual and predicted. rpart")


#It looks like the decision tree model is the more accurate of the two models



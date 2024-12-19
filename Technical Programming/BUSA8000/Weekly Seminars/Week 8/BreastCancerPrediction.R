library(class)

#import data
breastcancerData <- read.csv("breast-cancer-wisconsin.data")


#Display structure of the data
str(breastcancerData)

#Label the dataset
names(breastcancerData) <- c("id","clump_thickness", "uniformity_size", "uniformity_shape",
                            "marginal_adhesion", "single_epithelial_cell_size", 
                            "bare_nuclei", "bland_chromatin", "normal_nucleoli",
                            "mitoses", "diagnosis")

str(breastcancerData)

#Data preperation
breastcancerData$id <- NULL

str(breastcancerData)

# bare_nuclei is Character
#Converting data into numeric format
breastcancerData$bare_nuclei <- as.numeric(breastcancerData$bare_nuclei)

#identify the rows without missing data
# we will reduce the number of observations
# ?complete.cases
breastcancerData <- breastcancerData[complete.cases(breastcancerData),]

#display the structure of our dataset (we have less observations)
str(breastcancerData)

#Transform diagnosis of 2 and 4 into benign and malignant
breastcancerData$diagnosis <- factor(ifelse(breastcancerData$diagnosis ==2, "benign", "malignant"))

#Build the model
#Data splicing
trainingset <- breastcancerData[1:477, 1:9]
testset <- breastcancerData [478:682, 1:9]

#split the diagnosis into training and test outcome sets
trainingOutcomes <- breastcancerData[1:477, 10]
testOutcomes <- breastcancerData [478:682, 10]

#Apply KNN algorithm to trainingSet and trainingOutcomes
predictions <- knn(train = trainingset, cl = trainingOutcomes, k = 21, 
                   test = testset)
#Display predictions
predictions

#Model Evaluation
table(testOutcomes, predictions)

#Finding accuracy
actuals_preds <- data.frame(cbind(actuals=testOutcomes, predicted=predictions))
correlation_accuracy <- cor(actuals_preds)
head(actuals_preds)

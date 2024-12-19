#### Week 7 Lecture (Example 2) ####

library(tidyverse)
library(class)

k_means_data=read_csv(file="wk7_data.csv") 
#load data into R

head(k_means_data) 
#quickly inspect data again

k_means_data=k_means_data %>%
  select(-ID,-Classification) 
#for the purposes of this exercise, remove columns 1 and 4 (unsupervised learning no labels)

#let's make a quick plot of the data 
ggplot() + 
  geom_point(data=k_means_data,aes(x=Factor_1,y=Factor_2)) +
  xlab("Factor 1") +
  ylab("Factor 2") +
  ggtitle("Sample data") +
  theme(plot.title = element_text(hjust = 0.5)) +
  #centralize the title of the plot
  xlim(1,6) +
  #set the lower and upper limits of the x-axis
  ylim(0.5,6.5)
  #set the lower and upper limits of the y-axis 

clustering=kmeans(k_means_data,3) 
#Use the kmeans function to run the k-means 
#clustering algorithm and choose k = 2
?kmeans
clustering
#see the output from the kmeans function
#obtain a bunch of 1's and 2's representing
#the assigned clusters for our data 

class(clustering)
#the class function returns the type of object used 
#as an input or argument. 
#for example, the clustering object here 
#is a "kmeans" object.
#A lot of basic techniques we have seen also
#work on this class.
#In particular, the available components behave
#like columns in a tibble, so we can use the $ sign 
#to extract information from the available components.

#For example, extract "cluster" from "available components", group 1 or 2
clustering$cluster 

clustering$size 
#size of each cluster
#one cluster has 792 individual observations, 
#and the other cluster has 400.

clustering$centers 
#the two centers of the clusters, the centroids of our final clusters

clustered_data = k_means_data %>%
  mutate(Classification = clustering$cluster) 
#merge the clustering output with the original data set
#by adding an additional column "Classification"

#?kmeans

head(clustered_data) 
#inspect the merged data

clustered_data$Classification=
  as.character(clustered_data$Classification) 
#change to characters since the cluster number 
#should be a categorical variable

head(clustered_data) 
#inspect the merged data again

#Let's make a plot
ggplot() +
  geom_point(data=clustered_data,
             aes(x=Factor_1,y=Factor_2,
                 color=Classification),alpha=0.1) +
  #plot the data from the clustered_data object
  #set the opacity as 10%
  geom_point(data=as.data.frame(clustering$centers),
             aes(x=Factor_1,y=Factor_2),shape=4)
  #plot the centers of the clusters
  #get the centers by using clustering$centers
  #the geom_point function requires the data in 
  #a tibble format. 
  #use the as.data.frame function to convert 
  #it to a tibble
  #change the icon used in the graph by 
  #adjusting the shape parameter, say shape=4

#the graph gives a teal cluster and a red cluster, 
#as well as the centers of the two clusters 
#plotted as crosses.

#save the output as a csv file
write_csv(clustered_data,"Clean_Results.csv")


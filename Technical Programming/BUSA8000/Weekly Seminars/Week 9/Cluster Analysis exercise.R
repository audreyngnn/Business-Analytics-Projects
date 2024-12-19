#https://www.youtube.com/watch?v=MAUs4484TG8

#To load the package "factoextra", we need to install and load the package "ggplot2" first
install.packages("ggplot2")
library(ggplot2)

install.packages("factoextra")
# package that provides a set of functions for exploratory data analysis
# and visualization of multivariate data
library(factoextra)

#view the iris data (Built-in Dataset in R)
iris

#create a new variable iris.labels that contains the same species labels 
#as the iris$Species variable, but as a factor instead of a character vector.
iris.labels <- iris$Species

#view the structure of the data in the column "iris.labels"
str(iris.labels)

#creates a contingency table of the number of observations for each unique value 
#in the iris.labels vector.
table(iris.labels)

#select the first four columns of the iris data set.
#corresponds to the sepal length, sepal width, petal length, and petal width 
#measurements for each observation.
iris_data = iris[1:4]


# Scale
# standardise the four columns of iris_data so that each column has a mean of zero and a standard deviation of one. 
# The resulting object, iris_data_std, is a standardized version of the iris_data
iris_data_std = scale(iris_data)

#Distance
#calculate the Euclidean distance between each pair of rows/observations in the data frame. 
#Euclidean distance is a common distance measure used in machine learning algorithms
iris.dist = dist(iris_data_std)

#hierarchical clustering algorithm
#To perform hierarchical clustering, 
#the technique used to group objects or observations is based on their similarity or dissimilarity. 
#hierarchical clustering is used to group the iris flowers based on their physical characteristics.
hc.out_iris <- hclust(iris.dist, method = "complete")
hc.out_iris

?hclust

#plot the dendrogram (i.e., a tree-based diagram)
plot(hc.out_iris)

#draw a rectangle around the clusters formed by cutting the hierarchical clustering dendrogram at a specified height
#k = 3 specifies the number of clusters to cut the dendrogram into 
#border = 2:5 specifies the border colors for the rectangles that will be drawn around the clusters
rect.hclust(hc.out_iris, k = 3, border = 2 : 5)

#choose other border colors
rect.hclust(hc.out_iris, k = 3, border = 3 : 6)

#Clusters
#iris.clusters object is a vector of integers 
#assigns each observation in the iris data set to one of the three clusters formed
#extract the clusters formed by hierarchical clustering and assigning each observation to a specific cluster
iris.clusters <- cutree(hc.out_iris, k=3)
length(iris.clusters)

#visualise the cluster

#obtain the row names of the standardized iris dataset
#create a vector of new row by concatenating the species name (from the original iris dataset) 
#use the row number (1 to the number of rows in the iris dataset, obtained with dim(iris)[1]) 
rownames(iris_data_std) <- paste(iris$Species, 1:dim(iris)[1], sep = "_")

?fviz_cluster
#fviz_cluster is a function from the R package "factoextra" thats Visualises Clustering Results
#fviz_cluster is called with a list of two arguments
#a named list with the data set to be clustered, iris_data_std
#the second argument is a vector of cluster assignments for each observation in the iris_data_std data set
fviz_cluster(list(data=iris_data_std, cluster = iris.clusters))

#cross-tabulate these two variables to show how many observations 
#belong to each cluster-species combination.
table(iris.clusters, iris$Species)



clust <- read.csv("book1.csv",header=F, sep=",")



# assign row names and column names
cnames <- c("country","wine","heart")
colnames(clust) <- cnames
rownames(clust) <-clust$country


# Hierarchical Clustering
# Create the distance matrix by calculating the pairwise Euclidean between observations
d <- dist(clust, method = "euclidean") 
fit <- hclust(d)
# display the dendrogram 
plot(fit)


groups <- cutree(fit, k=5) # cut tree into 5 clusters
# draw the dendrogram with red borders around the 5 clusters 
rect.hclust(fit, k=5, border="red")

# create a scatter plot of two variables
plot(clust$wine,clust$heart)
text(x=clust$wine, y=clust$heart, labels=clust$country, col=groups)


# K means
# we want to identify 3 clusters
# we specify 10 number of random starts
clustk <- kmeans(clust[,c("wine","heart")], centers=3, nstart=10)
clustk

# create a scatter plot of two variables
plot(clust$wine, clust$heart, xlab="wine", ylab="heart")
text(x=clust$wine, y=clust$heart, labels=clust$country,col=clustk$cluster+1)


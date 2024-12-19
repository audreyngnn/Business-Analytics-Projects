#Step 1 have your data or file ready
#http://www.sthda.com/english/wiki/text-mining-and-word-cloud-fundamentals-in-r-5-simple-steps-you-should-know
#https://www.red-gate.com/simple-talk/databases/sql-server/bi-sql-server/text-mining-and-sentiment-analysis-with-r/



#Step 2 Install and load the required packages

install.packages("tm")  # for text mining
install.packages("SnowballC") # for text stemming
install.packages("wordcloud") # word-cloud generator (e.g. generate word-cloud plots) 
install.packages("RColorBrewer") # color palettes
install.packages("NLP") # Natural Language Processing 

#Load packages
#The "tm" package is used for text mining and 
#provides various functions and tools for text pre-processing, 
#manipulation, and analysis
library("tm")
#NLP is required for SnowballC  
library("NLP")
#package provides stemming algorithms for multiple languages. 
#Stemming is the process of reducing words to their base or root form, 
#which can be useful for text analysis tasks 
library("SnowballC")
#package offers a collection of color palettes 
#that can be used for data visualization 
library("RColorBrewer")
#Note that RColorBrewer is required for wordcloud
library("wordcloud")


#Step 3 Load the text file
#The text is loaded using Corpus() function from text mining (tm) package. 
#In R, a Corpus is a collection of text document(s) 
#to apply text mining or NLP routines on.

#read the contents of a text file into an R variable named "text"
text <- readLines(file.choose())

#Load the data as a corpus
docs <- Corpus(VectorSource(text))

# Read the text file from internet
filePath <- "http://www.sthda.com/sthda/RDoc/example-files/martin-luther-king-i-have-a-dream-speech.txt"
text <- readLines(filePath)


#Inspect the content of the document
inspect(docs)

#Transform the text
#Transformation is performed using tm_map() function 
#to replace, for example, special characters from the text.
#Replacing "/", "@" and "|" with space:
#The tm_map() function is used to apply a transformation function 
#to each document in the corpus.

toSpace <- content_transformer(function (x , pattern ) gsub(pattern, " ", x))
docs <- tm_map(docs, toSpace, "/")
docs <- tm_map(docs, toSpace, "@")
docs <- tm_map(docs, toSpace, "\\|")

#Cleaning the text
#the tm_map() function is used to remove unnecessary white space, 
#to convert the text to lower case, 
#to remove common stopwords like "the", "we"

# Convert the text to lower case
docs <- tm_map(docs, content_transformer(tolower))
# Remove numbers
docs <- tm_map(docs, removeNumbers)
# Remove english common stopwords
#The stopwords() function is used to retrieve a list of common English stopwords. 
#Stopwords are words that are commonly used in a language 
#but do not carry much significance in the context of text analysis. 
#Examples of English stopwords include "the", "is", "and", "a", etc.
docs <- tm_map(docs, removeWords, stopwords("english"))
# Remove your own stop word
# specify your customized stopwords as a character vector
docs <- tm_map(docs, removeWords, c("blabla1", "blabla2")) 
# Remove punctuation
docs <- tm_map(docs, removePunctuation)
# Eliminate extra white spaces
docs <- tm_map(docs, stripWhitespace)
# Text stemming
# docs <- tm_map(docs, stemDocument)

#Step 4 Build the term document matrix
#Document matrix is a table containing the frequency of the words. 
#Column names are words and row names are documents. 
#The function TermDocumentMatrix() from text mining package can be used as follow :

# Build a term-document matrix
dtm <- TermDocumentMatrix(docs)
m <- as.matrix(dtm)
# Sort by decreasing value of frequency
v <- sort(rowSums(m),decreasing=TRUE)
d <- data.frame(word = names(v),freq=v)
# Display the top 10 most frequent words
head(d, 10)


#Step 5 Generate the Word cloud
set.seed(1234) # size
wordcloud(words = d$word, freq = d$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))


#words : the words to be plotted
#freq : their frequencies
#min.freq : words with frequency below min.freq will not be plotted
#max.words : maximum number of words to be plotted
#random.order : plot words in random order. 
#If false, they will be plotted in decreasing frequency.
#rot.per : proportion words with 90 degree rotation (vertical text)
#colors : color words from least to most frequent. 
#Use, for example, colors "black" for single color.


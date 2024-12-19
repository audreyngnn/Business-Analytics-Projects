#### Lecture Week 2 ####


#A quick look at the R Studio Interface 
#Script: write, edit and save code
#Console: write and execute code, print and save the output
#Environment: record the R objects and their values in Console
1+1 #calculate the sum
y<-1+1 #calculate the sum and save the output to the R object y
y #print the R object y 
#calculate the sum and save the output to the R object y
y #print the R object y 
y<-8 #overwrite the value of the R object y
y #print the R object y to see its new value
y=10 #overwrite the value of the R object y
y #print the R object y to see its new value



# install.packages(tidyverse) 
#does not work. Why?
#tidyverse is a name/string, but not an object
# install.packages("tidyverse")
#Use "" to tell R that tidyverse is a name/string.
install.packages(c("zoo","tidyverse"))
#download and install the two packages at the same time (save time)
#using the concatenate function c() 
library(zoo)
library(tidyverse)
#load the two packages 


#Use the function read_csv() in tidyverse to import the data set in R
#the function read.csv() can be used as well.

#sample_marks=read_csv(file="H:/teaching/BUSA8000/week 2 slides/sample_data.csv") 
#"H:\teaching\BUSA8000\week 2 slides\sample_data.csv" 
# is the location of the file in the computer
#Change backslash "\" to forward lash "/"

#place the .R file consisting of the R scripts in the same folder
#as the data file "\sample data.csv"
sample_marks=read_csv(file="sample_marks.csv")
#load data into R and save the data in the R object
sample_marks #see the tibble
str(sample_marks) #this will tell you the types of data in each column



#There are different ways to return the OL_Quiz_1 mark for Romeo:

sample_marks[3,4] #note this returns the mark as a tibble (a tibble)
sample_marks$OL_quiz_1[3] #the dollar sign $ can be used to specify a column (a number)


#What if we do not know the index/location? 
#for example, when the data set is large

filter(sample_marks,First_Name == "Romeo")$OL_quiz_1 
#note the use of double equal signs "==" different from "=" or "<-"
#First_Name == "Romeo" is a logical statement
#to check whether First_Name is Romeo.
#Filter would find all students with first name Romeo
#in the tibble sample_marks.

sample_marks %>% #this is a Pipe or a Pipe Operator, 
#which is used to perform a sequence of instructions
#within the tibble sample_marks.
#we can add separate individual instructions below
  filter(First_Name == "Romeo") %>%
  #filter chooses the row Romeo
  select(OL_quiz_1)
  #select chooses the column OL_quiz_1

#when the dollar sign $ is used, the mark is returned as 
#a number rather than a tibble.



#Similarly, there are a few ways to return all data for Romeo 
#in Row 3.

sample_marks[3,] #this returns the data as a tibble.

sample_marks[,3]

filter(sample_marks,First_Name == "Romeo")

sample_marks %>% #piping technique
  filter(First_Name == "Romeo")

#these also returns the data as a tibble.



#To retrieve all final exam marks

sample_marks[,7] #returns a tibble -- using index

sample_marks$Final_exam #returns a vector of numbers -- using name



#To retrieve First Names, Surnames, and Final exam marks together

sample_marks[,c(2,3,7)] #return columns 2, 3, and 7 as a tibble
#the function c() (the concatenate function) 
#puts together the numbers 2, 3, 7 as a vector (Tutorial Week 2).



select(sample_marks,Surname,First_Name,Final_exam)

sample_marks %>% #piping technique
  select(Surname,First_Name,Final_exam)

#these returns the three columns as a tibble.



#Dealing with missing values (NA's, cleaning data = finding empty values)

anyNA(sample_marks) #checks if any NA's exist
is.na(sample_marks) 
#test each entry in the tibble for NA's and
#return a tibble with entries as either "TRUE" or "FALSE"
#FALSE is assigned 0 and TRUE is assigned 1.
sum(is.na(sample_marks)) #count the number of NA's
colSums(is.na(sample_marks)) #count the NA's by column
which(is.na(sample_marks)) #find which entry in Report column is NA

filter(sample_marks, is.na(sample_marks$Report)) # only show the records where Report is NA

sample_marks %>%
  filter_all(any_vars(is.na(.)))  # show records with NA in any column

sample_marks2 = smaple_marks
sample_marks2$Final_Exam[3]=NA
sample_marks2

sample_marks2 %>%
  filter_all(any_vars(is.na(.)))


#Filtering for final exam marks > 65

filter(sample_marks,Final_exam >= 65)
#filter would find all the rows in sample_marks with Final_exam >= 65
#and return the rows in a tibble.

sample_marks %>% #piping method
  filter(Final_exam >= 65)

#if you're only interested in names of these students
sample_marks %>% #piping method
  filter(Final_exam >= 65) %>%
  select(Surname,First_Name) 



#Filtering text data

sample_marks$Student_ID 
#this would extract the student ID's
substr(sample_marks$Student_ID,1,1) 
#this would take the first digit of each ID
substr(sample_marks$Student_ID,1,2) 
#this would take the first two digits of each ID
filter(sample_marks,substr(sample_marks$Student_ID,1,1)==1) 
#filter for student ID's starting with 1
#Do the same thing using Pipe
sample_marks %>% #piping technique
  filter(substr(sample_marks$Student_ID,1,1)==1)
#filter for student ID's starting with 1

grep("1",sample_marks$Student_ID) 
#picks out rows where ID contains a 1
grep("^1",sample_marks$Student_ID) 
#picks out the rows where ID starts with 1
#To type ^, press shift + 6
sample_marks[grep("^1",sample_marks$Student_ID),] 
#use the grep function to select rows 
#with student ID's starting from 1


?prep #?<function name> to find out how to use a function


#Calculate mean and median

mean(sample_marks[,4]) 
#this will not work. Why?
#sample_marks[,4] gives a tibble.
mean(sample_marks$OL_quiz_1) #calculate mean OL_Quiz_1 mark
median(sample_marks$OL_quiz_1) #calculate median OL_Quiz_1 mark

#Calculate filtered mean

filter(sample_marks,Final_exam>=65)$OL_quiz_1 
#return the OL_Quiz_1 marks for students 
#who scored 65 or more in the final exam
mean(filter(sample_marks,Final_exam>=65)$OL_quiz_1) 
#calculate the mean for these students



#Dealing with missing entries

mean(sample_marks$Report) 
#this will return "NA", why?
#The column Report contains NA.
mean(sample_marks$Report,na.rm=TRUE) #na.rm = remove na from the column
#calculate the mean, but ignore NA's



#The ID column is currently reading as numbers. 
#Let's convert to characters (text)

sample_marks$Student_ID #view the ID's
as.character(sample_marks$Student_ID) 
#change the ID's as characters, but not yet saved them
sample_marks$Student_ID = as.character(sample_marks$Student_ID)
#save the changes
sample_marks$Student_ID 
#the ID's now have quotation marks, (i.e. characters)



#Add a new student using the function add_row() 

sample_marks_2=sample_marks %>%
  add_row(Student_ID="5574",Surname="Snow",First_Name="Jon",OL_quiz_1=83,
          Report=68,OL_quiz_2=80,Final_exam=78)
#add a new row for the new student and save it in a new name

sample_marks_2 #view updated version

# what if I miss a column
sample_marks_2=sample_marks %>%
  add_row(Student_ID="5574",Surname="Snow",OL_quiz_1=83,
          Report=68,OL_quiz_2=80)

sample_marks_2



#Changing Mister Bean's Report mark to 62

select(filter(sample_marks,First_Name=="Mister"),Report) 
#this will get Mister Bean's Report mark as a tibble

select(filter(sample_marks,First_Name=="Mister"),Report)=62 
#this won't work because you assign a number to a tibble


#We need the mutate() and replace() functions

sample_marks %>% #pipe technique
  mutate(Report = replace(Report, First_Name == "Mister", 62)) 
#only apply if First_Name == "Mister"
#this will create a new tibble, but not change the original tibble

sample_marks_3=sample_marks_2 %>% #save the updated version as sample_marks_3
  mutate(Report = replace(Report, First_Name == "Mister", 62)) 

sample_marks_3 #view the updated version
sample_marks_2 # view the original one



#Add 3 marks to all Final_exam marks using mutate, as we did above

sample_marks_4 = sample_marks_3 %>%
  mutate(Final_exam = replace(Final_exam,TRUE,Final_exam+3)) 
#the TRUE just means apply to all rows (all observations in Final_exam)
sample_marks_4 #view the updated version




#Adding a final grade column using mutate()

sample_marks_5 = sample_marks_4 %>%
  mutate(Final_Grade = 0.1*OL_quiz_1+0.1*OL_quiz_2
         +0.2*Report+0.6*Final_exam) 
#create a new column Final_Grade
#note that the mutate function knew we were creating a new column
#when Final_Grade was not in the previous list of column.
sample_marks_5 #view the updated version

# ??? what if you want to replace all missing values with 0
# investigate replace_na function
?replace_na

sample_marks_5$Final_Grade %>% replace_na(0)

# if NAs in many columns
sample_marks_5 %>% replace_na(list(Final_exam=10, Final_Grade=0))  # use different filling value for different columns


sample_marks_5 %>%
  filter(OL_quiz_2 > 90) %>%
  mutate(Final_exam = replace_na(Final_exam, 10), Final_Grade = replace_na(Final_Grade,0)) 

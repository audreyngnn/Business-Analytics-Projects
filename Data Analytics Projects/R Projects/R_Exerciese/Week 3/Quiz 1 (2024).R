library(tidyverse)

data_scientist=read_csv(file="data_scientist_hr.csv") 
str(data_scientist)
head(data_scientist)

# Question 2
df1 = data_scientist
df1$gender[4]=NA
df1

df1 %>%
  filter_all(any_vars(is.na(.)))

filter(df1,gender == "Male")

# Question 3
df2 = data_scientist
df2$education_level[7]=NA
df2

df2 = filter(df2,gender == "Female")
filter(df2,education_level == "Phd")

# Question 4
df3 = data_scientist
df3$experience[9]=NA
df3

df3 <- df3 %>%
  mutate(`experience` 
       = replace(`experience`, `experience` 
                   == ">20","20")) %>% 
  mutate(`experience` = as.integer(`experience`)) 

unique(df3$`experience`) 

df4 = filter(df3,experience > 10)


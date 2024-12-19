#### Week 3 (Data Visualisations) ####
library(tidyverse)
library(zoo)
library(viridis) # provides a set of color palettes for your ggplot visualizations

temperature_table=read_csv(file="Climate_data.csv")

head(temperature_table) 
#inspect the data by printing the first few rows

#the first two and last columns will not be used here, drop them

temperature_table = temperature_table %>%
  select(-'Product code',-'Bureau of Meteorology station number'
         ,-Quality) #drop the three columns

head(temperature_table) 
#the three columns are removed.

#combine year and month to make a date column

temperature_table = temperature_table %>%
  mutate(Date = as.yearmon(paste(temperature_table$Year,
  temperature_table$Month,sep="-")))
#mutate is used to create a new column date.
#note that the function as.yearmon is from the zoo package.
#it is used to combine year and month into date. 

head(temperature_table) 
#the new column date is created. 

#Rename temperature column for convenience

temperature_table = temperature_table %>%
  rename(Temp = `Mean maximum temperature (°C)`)

head(temperature_table) 
#inspect data again
#the temperature column is renamed.

#Let's start with a scatterplot of the temperatures against year
#use the ggplot package which is a part of the tidyverse package

ggplot(temperature_table) + 
  #enter our data into ggplot, + means we're adding more things
  #+ acts like a Pipe (or a Pipe operator), 
  #but we use + instead of %>%
  geom_point(aes(x=Year, y=Temp))+ 
  #geom_point gives a scatterplot
  #the aesthetic specification "aes" is used to specify 
  #the x-axis and the y-axis.
  xlab("Year") + #label the x-axis
  ylab("Temperature") + #label the y-axis
  ggtitle("Average max temperatures by year") 
  #give a title to the graph

#notice the title is to the left. 
#we can run the following code to make it centered. 
theme_update(plot.title = element_text(hjust = 0.5))



###Adding these elements can significantly improve the readability and informative value of your plot
ggplot(temperature_table, aes(x = Year, y = Temp)) + 
  geom_point(aes(color = Month), alpha = 0.7, size = 3) + 
  geom_smooth(se = FALSE, method = "loess", color = "blue") + # For noisy data, consider adding a smoothed line using geom_smooth() to show trends more clearly. ## Loess fits multiple regressions
  scale_color_viridis_d() + # used to adjust the plot to use color scales in a meaningful way
  labs(
    x = "Year",
    y = "Temperature",
    title = "Average Max Temperatures by Year",
    subtitle = "With Trend Line and Category Differentiation" ) +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5),legend.position = "bottom") +
  guides(color = guide_legend(title = "Month")) #customizes the legend title for the color aesthetic to "Month". 
# This is useful when you have mapped a variable to color in your plot and want the legend to clearly indicate what the colors represent, which in this case would be the months.




#now let's make a histogram of the temperatures observed.
ggplot(temperature_table) +
  geom_histogram(aes(x=Temp,fill=..count..),
  stat="bin",binwidth=0.5) + 
  #geom_histogram plots a histogram.
  #note that in the histogram, the x-axis is the temperature value
  #and the y-axis is the respective frequency. 
  #fill=..count.. fills color depending on the number of occurrence
  #(or the frequency) of a particular temperature value.  
  #geom_bar gives bar graph, and the fill colour depends on count
  #stat="bin" groups the temperature data into bins of the histogram.
  #note that the bins are of equal length.
  #binwidth=0.5 specifies the width of each bin. 
  xlab("Temperature") + #label the x-axis
  ggtitle("Histogram of observed temperatures") + 
  #give the histogram a name
  theme_light() + 
  #change background colour
  scale_fill_continuous("frequency") 
  #choose the colour scheme


###Adding these elements can significantly improve the readability and informative value of your plot
ggplot(temperature_table, aes(x=Temp)) +
  geom_histogram(binwidth=0.5, aes(fill=..count..)) +
  geom_vline(aes(xintercept=mean(Temp, na.rm=TRUE)), color="blue", linetype="dashed", size=1) + ### Overlaying a vertical line indicating the mean or median temperature can provide 
  #immediate insight into the distribution's central tendency. 
  #Use geom_vline() with xintercept = mean(temperature_table$Temp) or median(temperature_table$Temp).
  scale_fill_gradient(low="lightblue", high="darkblue", name="Frequency") +
  labs(x="Temperature (°C)", y="Frequency", title="Histogram of Observed Temperatures") +
  theme_light() +  #When you add theme_light() to your ggplot chain, it modifies the plot's overall appearance by setting a series of theme elements.
  theme(text=element_text(size=12), axis.title=element_text(size=14), title=element_text(size=16, face="bold")) +
  scale_x_continuous(breaks=seq(min(temperature_table$Temp), max(temperature_table$Temp), by=1)) + # Format x-axis (if needed)
  scale_y_continuous(labels=scales::comma) # Format y-axis labels (if needed)



#we now make some a boxplot by month
ggplot(temperature_table) +
  geom_boxplot(aes(x=Month, y=Temp)) + 
  #force R to read months as a categorical variable
  xlab("Month") +
  #label the x-axis
  ylab("Temperature") +
  #label the y-axis 
  ggtitle("Temperatures by month")
  #give the title of the boxplot 



###Adding these elements can significantly improve the readability and informative value of your plot
# Assuming temperature_table$Month is already converted to a factor with the correct order
ggplot(temperature_table, aes(x=Month, y=Temp, fill=Month)) + 
  geom_boxplot() +
  geom_jitter(width=0.2, alpha=0.5) +  # Add jittered points, this is particularly useful for visualizing the distribution of data points where you have many overlapping points
  scale_fill_brewer(palette="Spectral") +  # Color by 'Month' with a nice palette
  theme_minimal() +  # Use a minimal theme - provides a clean and modern appearance by removing background clutter and focusing on the data. 
  theme(axis.text.x=element_text(angle=45, hjust=1)) +  # Rotate x-axis labels for better legibility
  labs(x="Month", y="Temperature", title="Temperatures by Month", fill="Month") +  # Customize labels
  scale_y_continuous(labels=scales::comma)  # Format y-axis labels (if needed)



#Finally, let's make a line plot.
#Let's calculate the average temp in each year, 
#and plot that against the year. 

annual_mean_temp <- group_by(temperature_table,Year) %>% 
  #group the temperature data based on year
  summarise(mean_temp=mean(Temp)) 
  #calculate mean temp within each group (year)

head(annual_mean_temp) 
#inspect new tibble and see that the group means 
#(or the annual means) have been calculated


ggplot(annual_mean_temp) +
  geom_line(aes(x=annual_mean_temp$Year,
  y=annual_mean_temp$mean_temp),color="blue") + 
  #geom_line gives the line plot
  xlab("Year") +
  #label the x-axis
  ylab("Temperature") +
  #label the y-axis 
  ggtitle("Annual average daily max temperature")
  #give the line plot a title 


###Adding these elements can significantly improve the readability and informative value of your plot
ggplot(annual_mean_temp, aes(x=Year, y=mean_temp)) +
  geom_line(color="blue") + 
  geom_point(color="red") +  # this can help highlight individual data points on the line, making it easier to identify specific values or outliers.
  geom_smooth(se=TRUE, color="darkgreen", method="loess") +  # For noisy data, consider adding a smoothed line using geom_smooth() to show trends more clearly. ## Loess fits multiple regressions
  ggtitle("Annual Average Daily Max Temperature") +
  xlab("Year") + 
  ylab("Temperature (°C)")





# Youtube Trends
#### Big Data 44517, Section 1
#### Pair 1: Chase Smith, Kevin Hart
#### Pair 2: Jacob Taylor, Kaleb Odle

## Links
Dataset available at: https://www.kaggle.com/datasnaek/youtube-new

## Introduction
#### Youtube is the most widely known and popular video sharing service on the internet. This means there is a plethora of data available to pull from it. This project will deal with finding various "big data elements" (such as count or maximum) from Excel sheet(s) of pulled Youtube data.

## Data Source
#### The data source is multiple excel documents that each provide youtube data for a specific country. We will be using the USvideos.csv file as our specific source. The format is structed and the time range is from November 2017 to May 2018. The USvideos.csv file itself is 61 mb.

#### https://www.kaggle.com/datasnaek/youtube-new

## The Challenge
  #### Volume: There are over 40,000 rows with 16 columns for each row making a total of ~640,000 records.
  #### Variety: The data is in a structued excel spreadsheet. 
  #### Velocity: The data is at rest. 
  #### Veracity: The data was gathered from the YouTube API so the statictics will be trustworthy.
  #### Value: Video statistics on trending videos are useful for people who make other content to see what is popular. Its also impornant for people who make money off of the trending content and for the advertisers to see what categories people watch the most.

## Big Data Questions
  #### Kevin: For each channel in the US find the total number of views.
  #### Chase: For each channel in the US find the total number of dislikes.
  #### Jacob:
  #### Kaleb: For each channel in the US find the max number of comments.

## Big Data Solutions
  #### Mapper Input:
  #### Mapper Output/ Reducer Output:
  #### Reducer Output:
  #### Language: We will be using Python for MapReduce implementation.
  #### Charts: We will most likely be using column charts for the visualizations. If there is much variance between values, then a boxplot might be used as well or instead.

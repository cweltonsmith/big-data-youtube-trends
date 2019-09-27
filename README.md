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
  #### Kevin: For each channel with trending videos in the US find the total number of views.
  #### Chase: For each channel with trending videos in the US find the total number of dislikes.
  #### Jacob:
  #### Kaleb: For each channel with trending videos in the US find the max number of comments.

## Big Data Solutions
  #### Mapper Input:
    
    Kevin Hart:
    2kyS6SvSYSE	17.14.11	WE WANT TO TALK ABOUT OUR MARRIAGE	CaseyNeistat	22	2017-11-13T17:13:01.000Z	SHANtell martin	748374	57527	2966	15954	https://i.ytimg.com/vi/2kyS6SvSYSE/default.jpg	FALSE	FALSE	FALSE	SHANTELL'S CHANNEL - https://www.youtube.com/shantellmartin\nCANDICE - https://www.lovebilly.com\n\nfilmed this video in 4k on this -- http://amzn.to/2sTDnRZ\nwith this lens -- http://amzn.to/2rUJOmD\nbig drone - http://tinyurl.com/h4ft3oy\nOTHER GEAR ---  http://amzn.to/2o3GLX5\nSony CAMERA http://amzn.to/2nOBmnv\nOLD CAMERA; http://amzn.to/2o2cQBT\nMAIN LENS; http://amzn.to/2od5gBJ\nBIG SONY CAMERA; http://amzn.to/2nrdJRO\nBIG Canon CAMERA; http://tinyurl.com/jn4q4vz\nBENDY TRIPOD THING; http://tinyurl.com/gw3ylz2\nYOU NEED THIS FOR THE BENDY TRIPOD; http://tinyurl.com/j8mzzua\nWIDE LENS; http://tinyurl.com/jkfcm8t\nMORE EXPENSIVE WIDE LENS; http://tinyurl.com/zrdgtou\nSMALL CAMERA; http://tinyurl.com/hrrzhor\nMICROPHONE; http://tinyurl.com/zefm4jy\nOTHER MICROPHONE; http://tinyurl.com/jxgpj86\nOLD DRONE (cheaper but still great);http://tinyurl.com/zcfmnmd\n\nfollow me; on http://instagram.com/caseyneistat\non https://www.facebook.com/cneistat\non https://twitter.com/CaseyNeistat\n\namazing intro song by https://soundcloud.com/discoteeth\n\nad disclosure.  THIS IS NOT AN AD.  not selling or promoting anything.  but samsung did produce the Shantell Video as a 'GALAXY PROJECT' which is an initiative that enables creators like Shantell and me to make projects we might otherwise not have the opportunity to make.  hope that's clear.  if not ask in the comments and i'll answer any specifics
    
    Chase Smith:
    1ZAPwfrtAFY	17.14.11	The Trump Presidency: Last Week Tonight with John Oliver (HBO)	LastWeekTonight	24	2017-11-13T07:30:00.000Z	last week tonight trump presidency|"last week tonight donald trump"|"john oliver trump"|"donald trump"	2418783	97185	6146	12703	https://i.ytimg.com/vi/1ZAPwfrtAFY/default.jpg	FALSE	FALSE	FALSE	One year after the presidential election, John Oliver discusses what we've learned so far and enlists our catheter cowboy to teach Donald Trump what he hasn't.\n\nConnect with Last Week Tonight online...\n\nSubscribe to the Last Week Tonight YouTube channel for more almost news as it almost happens: www.youtube.com/user/LastWeekTonight\n\nFind Last Week Tonight on Facebook like your mom would: http://Facebook.com/LastWeekTonight\n\nFollow us on Twitter for news about jokes and jokes about news: http://Twitter.com/LastWeekTonight\n\nVisit our official site for all that other stuff at once: http://www.hbo.com/lastweektonight


  #### Mapper Output/ Reducer Output:

    Kevin Hart:
    CaseyNeistat   748374.0
    
    Chase Smith:
    LastWeekTonight   6146.0

  #### Reducer Output:

    Kevin Hart:
    CaseyNeistat    232745266.0
    
    Chase Smith:
    LastWeekTonight   (31234.0)

  #### Language: We will be using Python for MapReduce implementation.

    Kevin Hart:
    I will be using Python for MapReduce.
    
    Chase Smith:
    I will be using Python for MapReduce.

  #### Charts: We will most likely be using column charts for the visualizations. If there is much variance between values,then a boxplot might be used as well or instead.

    Kevin Hart:
    I will make barchart showing the difference between the top 5 and lowest 5. 
    
    Chase Smith:
    I will make a pie chart for the top 10 trending videos with the most dislikes.

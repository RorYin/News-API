# News-API
Get all latest / related to topic NEWS as a JSON output

How to use?
<br>
Download the code on ur local pc and run app.py
You will see the app working on  👇 link on local server
<br>
``` 
 http://127.0.0.1:5000/  
```
Else if you wish to deploy to Heroku ,the link  will be 👇 (scroll down to see how to get ur baseurl)
 ```
 https://baseurl.herokuapp.com/
 ```
<br>
How to pass query
<br>
<br>

 
 ```
 Heroku: https://baseurl.herokuapp.com/?q=keyword
 Local Server: http://127.0.0.1:5000/?q=keyword
 ```

<br>
You can any one of the below keyword as query

Keywords:
<br>
```
top news
entertainment
world
business
education
technology
cricket
food
travel
viral
lifestyle  

Note:"top news" gives the top news of India 
```

Example :
```
Heroku: https://baseurl.herokuapp.com/?q=world
Local Server: http://127.0.0.1:5000/?q=world
```

You can also give any topic name as query , example:
```
Heroku: https://baseurl.herokuapp.com/?q=pubg
Local Server: http://127.0.0.1:5000/?q=pubg
```

Sample Responses:
```
[
  {
    "headline": "US Election 2020: Polls Begin in New York, New Jersey, Virginia; Americans Start Casting Ballots", 
    "image url": "https://s3.india.com/wp-content/uploads/2020/11/US-election-768x512.jpg#768#512", 
    "paragraph": "  US Presidential Elections: Over a 100 million Americans had already casted their ballots by Tuesday", 
    "source url": "https://www.india.com/news/world/us-presidential-election-2020-begin-in-new-york-new-jersey-virginia-americans-cast-ballots-polling-stations-donald-trump-joe-biden-4196287/"
  }, 
  {
    "headline": "Hot or Cold Weather May Have No Significant Effect on Covid-19 Spread: Study", 
    "image url": "https://s3.india.com/wp-content/uploads/2020/08/b83d081b50a938ca492a35742c4c7630-320x180.jpg#320#180", 
    "paragraph": "  The researchers noted that weather influences the environment in which the coronavirus must survive", 
    "source url": "https://www.india.com/news/world/hot-or-cold-weather-may-have-no-significant-effect-on-covid-19-spread-study-4196090/"
  }, 
  {
    "headline": "COVID-19 Super-spreading Events Like Large Gatherings Can Infect Over 6 People at Once: Report", 
    "image url": "https://s3.india.com/wp-content/uploads/2020/08/COVID-768x512.jpg#768#512", 
    "paragraph": "  In the research, the scientists defined super-spreaders as individuals who passed the virus to more than", 
    "source url": "https://www.india.com/news/world/covid-19-super-spreading-events-like-large-gatherings-can-infect-over-6-people-at-once-report-4195873/"
  }, 
  {
    "headline": "US Elections 2020: Stores Barricade Windows, Install Wooden Planks Fearing Post-Poll Violence", 
    "image url": "https://s3.india.com/wp-content/uploads/2020/11/uj-1-768x512.jpg#768#512", 
    "paragraph": "  While they are still open for shoppers, stores are all boarded up to ensure there is no room for looting", 
    "source url": "https://www.india.com/news/world/us-elections-2020-fearing-post-poll-violence-stores-barricade-windows-install-wooden-planks-4195723/"
  }
]

Note:This is a part of the actual response ,since the actual response is huge 
```
<br>

##  Please Note:This is for educational purposes only ,do not abuse it, by using it for any other purposes.
<br>


## Get your baseurl by deploying to heroku 👇
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/RorYin/News-API/tree/main)

<br>

## **Star the Repo in case you liked it :)**
### © [Dhanush N (RorYin)](https://github.com/RorYin)


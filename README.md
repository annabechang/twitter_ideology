# twitter_ideology
this repo contains code for estimating a YouTube video's ideology based on Twitter accounts that shared it. We estimate the Twitter account's ideology based on a list of accounts they follow. 

More detail can be found in the following work: 

Less partisan polarization in consumption of non-political YouTube videos compared to news and political videos: Evidence from online data in the U.S
```
@article{jqdfollowing,
    author  = " Wojcieszak, Magdalena and Chang, Rong-Ching and Menchen-Trevino, Ericka ", 
    title = "Less partisan polarization in consumption of non-political YouTube videos compared to news and political videos: Evidence from online data in the U.S",
    year    = 2024,
    journal = "JQD:DM"}
```

Disclaimer: due to the terms of service, I can not share the data. And this repository may not be reproducible due to the change in Twitter API.  

Our approach can be broken down into several steps below: 

###  Collecting Follower

We used a final list of 1,604 American politicians, journalists, and news media with their corresponding ideology scores from [Twitter score](https://github.com/sdmccabe/new-tweetscores).
The code for collecting followers can be found in [Parallel-follower-collection.py](Parallel-follower-collection.py)

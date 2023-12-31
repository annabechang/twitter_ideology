# twitter_slant 
this repo contains code for estimating a YouTube video's slant  based on Twitter accounts that shared it. We estimate the Twitter account's slant  based on a list of accounts they follow. 

More detail can be found in the following work: 

Less partisan polarization in consumption of non-political YouTube videos compared to news and political videos: Evidence from online data in the U.S
```
@article{jqdfollowing,
    author  = " Wojcieszak, Magdalena and Chang, Rong-Ching and Menchen-Trevino, Ericka ", 
    title = "Less partisan polarization in consumption of non-political YouTube videos compared to news and political videos: Evidence from online data in the U.S",
    year    = 2023,
    journal = "JQD:DM"}
```

Disclaimer: due to the terms of service, I can not share the data. And this repository may not be reproducible due to the change in Twitter API.  

Our approach can be broken down into several steps below: 

###  Collecting Follower

We used a final list of 1,604 American politicians, journalists, and news media with their corresponding slant  scores from [Twitter score](https://github.com/sdmccabe/new-tweetscores). The slant  scores for these elites range from  -0.925, i.e., most liberal, to 2.155, i.e. most conservative political elite. [Twitter score](https://github.com/sdmccabe/new-tweetscores) have used the NOMINATE score of 116th Congress members to show that despite the asymmetry, 0 is the point that separates left-leaning and right-leaning politicians, journalists, and news media. 

We collected all the followers of these 1,604 politicians, journalists, and news media on Twitter for a total of 16,472,360 unique followers and a total of 862,409,644 following relationships between the unique Twitter users and the 1,604 political elites. On average, we collected 562,196 followers per landmark (median 92,412, max 55,171,199).

The code for collecting followers can be found in [Parallel-follower-collection.py](Parallel-follower-collection.py)

### Slant Score

The slant score of a video ($` v`$) is the weighted average of the slant  of all political elites ($` \sum_{i=1}^{N_{pol}}`$) followed by the users ($` \sum_{u=1}^{N_u}`$) who tweeted the video($` v`$):

$$ v = \frac{ \sum_{u=1}^{N_u} \sum_{i=1}^{N_{pol}} Pscore_{i,u} }{N_u \cdot N_{pol} } $$

 $` Pscore(i,u) `$ denotes the slant  score of the politician, journalist, and/or a news media outlet $` i`$ followed by the user $` u`$, $` N_u`$ denotes the total number of users who tweeted the video, and $` N_{pol}`$ denotes the total number of politicians, journalists, or news media outlets followed by each user. 

 We used the code in [Parallel-follower-mapping-score.py](Parallel-follower-mapping-score.py) to mape the score between users to tweets. 



# Slant Validation

We validate our slant score using two sets of previously used and extensively validated scores from [(Auditing Partisan Audience Bias within Google Search)] and [Ad Fontes' Media Bias Chart](https://adfontesmedia.com/interactive-media-bias-chart/).

Our slant scores are consistent with outputs of other classification approaches, correlating at 0.88 or higher with slant scores based on Twitter following patterns (Auditing Partisan Audience Bias within Google Search) and on manual labeling of political slant of news organizations Ad Fontes Media. 

Additionally, we selected 7 channels for validation (Vox, CNN, The Guardian, Fox News, Breitbart News, One America News Network) and aggregated our individual video slant scores to the level of each channel.


| Channel Name               | Our Channel Score | Citation                   | Media Bias Ad Fontes |
|---------------------------|-------------------|-----------------------------|----------------------|
| Vox                       | -0.4225           | -0.555                      | -10.2344             |
| The Guardian              | -0.1177           | -0.389                      | -8.4778              |
| CNN                       | -0.2498           | -0.118                      | -8.3163              |
| The New York Times        | -0.2560           | -0.260                      | -7.7310              |
| Fox News                  | 0.5975            | 0.608                       | 13.5108              |
| One America News Network  | 0.8461            | 0.864                       | 16.2944              |



 

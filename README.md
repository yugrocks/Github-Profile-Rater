# Github-Profile-Rater
A level-wise github profile rater. Rates profiles from 1-200 such that similar profiles get same rating (Level).    
Requirements: Python 3.4, Sklearn, numpy 1.11.0, scrapy     

# How to Run:   
<code>$ cd Github-Profile-Rater    
<code>$ python predict.py [profile url or github handle] <code>    

# How it works:    
It shows you the level of your github profile between 1 and 200, where level 1 is least and level 200 is the best, with respect to the best current profiles on github.   
Similar profiles get a similar (or the same) level.     
The data of 10000 different users was taken from github (scrapped) and was clustered in 200 groups. The diferent features like number of stars, followers etc. were taken into account, and were weighted accordingly.    
K means clustering has been used to cluster the data after weighting the different features.    

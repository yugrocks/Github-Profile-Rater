# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GitscrapperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ProfileItem(scrapy.Item):
    num_followers = scrapy.Field()
    num_followings = scrapy.Field()
    num_repositories = scrapy.Field()
    num_stars = scrapy.Field()
    username = scrapy.Field(serializer=str)
    stars_received = scrapy.Field()
    forks = scrapy.Field()
    
    
    

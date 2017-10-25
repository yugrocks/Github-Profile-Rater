from scrapy.crawler import CrawlerProcess
import sys
import os
path = os.getcwd()
sys.path.append(path+"\github_scrapper\gitscrapper\gitscrapper\spiders")
from single_profile_scrapper import *

def scrapprofile(profileurl):
    with open("profileurl.txt", 'w') as file:
        file.write(profileurl)
    spider = Spider2()
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(spider)
    process.start()
    print("profile = ", profile)
    return profile

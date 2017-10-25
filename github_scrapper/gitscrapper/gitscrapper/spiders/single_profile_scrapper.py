from __future__ import absolute_import
import scrapy
from functools import partial
from scrapy.exceptions import CloseSpider
import logging

logging.getLogger('scrapy').propagate = False
profile = {}

class Spider2(scrapy.Spider):
    name = "singleprofilespider"
    total_profiles = 0
    stars_received = 0
    forks = 0
    repo_link = "?tab=repositories"
    followers_link = "?tab=followers"
    followings_link = "?tab=following"
    data = list()
    
    def start_requests(self):
        with open("profileurl.txt", 'r') as file:
            profile_url = file.read()
        start_urls = [
            profile_url,
        ]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # here give the first repos page
        url = response.url + self.repo_link
        self.stars_received = 0
        self.forks = 0
        # username
        username = response.css("span.p-nickname::text").extract_first().strip()
        for i in range(1):
            yield response.follow(url=url, callback=partial(self.parse_repos_page,0,0))
        

    def convert_to_int(self, string):
        # To convert numbers like 90k to int like 90000
        try:
            integer = int(string)
            return integer
        except:
            if 'k' in string:
                string = string.replace("k", "")
                integer = float(string)
                integer = integer*1000
                return int(integer)
    def int2(self, string):
        try:
            integer = int(string)
            return integer
        except:
            if ',' in string:
                integer = string.replace(",", "")
                integer = self.convert_to_int(integer)
                return integer

    def parse_repos_page(self, stars_received, forks, response):
        next_page = response.css("div.paginate-container span.disabled::text").extract_first()
        if next_page != "Next" :
            if not (next_page is None):
                href_to_next = response.css("a.next_page::attr(href)").extract_first().strip()
            repos_on_page = response.css("li.source")
            for repo in repos_on_page:
                star_and_fork = repo.css("a.muted-link::text").extract()
                star_svg_element = repo.css("svg.octicon-star")
                if len(star_and_fork) > 1:
                    if len(star_svg_element) != 0:
                        stars_received += self.int2(star_and_fork[1].strip())
                    else:
                        forks += self.int2(star_and_fork[1].strip())
                    if len(star_and_fork) > 3:
                        forks += self.int2(star_and_fork[3].strip())
            if not (next_page is None):
                yield response.follow(href_to_next, partial(self.parse_repos_page,stars_received, forks))
            else:
                username = response.css("span.p-nickname::text").extract_first().strip()
                # extracting some info from the same page
                spans = response.css("div.user-profile-nav span.Counter::text").extract()
                num_repositories = self.convert_to_int(spans[0].strip()); num_stars = self.convert_to_int(spans[1].strip())
                num_followers = self.convert_to_int(spans[2].strip()); num_followings = self.convert_to_int(spans[3].strip())
                profile["username"] = username
                profile["num_repositories"] = num_repositories
                profile["num_stars"] = num_stars
                profile["num_followers"] = num_followers
                profile["stars_received"] = stars_received
                profile["num_followings"] = num_followings
                profile["forks"] = forks            
                yield profile
        else:
                username = response.css("span.p-nickname::text").extract_first().strip()
                # extracting some info from the same page
                spans = response.css("div.user-profile-nav span.Counter::text").extract()
                num_repositories = self.convert_to_int(spans[0].strip()); num_stars = self.convert_to_int(spans[1].strip())
                num_followers = self.convert_to_int(spans[2].strip()); num_followings = self.convert_to_int(spans[3].strip())
                profile["username"] = username
                profile["num_repositories"] = num_repositories
                profile["num_stars"] = num_stars
                profile["num_followers"] = num_followers
                profile["stars_received"] = stars_received
                profile["num_followings"] = num_followings
                profile["forks"] = forks            
                yield profile

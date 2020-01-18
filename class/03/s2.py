# Run with
#
# scrapy runspider s2.py –t csv –o - > s2.csv


# A very bare minimum spider

from scrapy.spiders import Spider

class MySpider(Spider):
    name = 's2'
#     allowed_domains = ['craigslist.org']
    start_urls = [ "https://www.andrew.cmu.edu/user/sraja/multi/abe.html" ]
    
    def parse(self, response):
        item = {}
        item['first'] = response.xpath("//li[@class='first']/text()").extract()
        item['last'] = response.xpath("//li[@class='last']/text()").extract()
        return item
        
        
        

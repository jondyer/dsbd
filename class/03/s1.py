# Run with
#
# scrapy runspider s1.py –t csv –o - > s1.csv


# A very bare minimum spider

from scrapy.spiders import Spider

class MySpider(Spider):
    name = 's1'
#     allowed_domains = ['craigslist.org']
    start_urls = [ "https://www.andrew.cmu.edu/user/sraja/multi/main.html" ]
    
    def parse(self, response):
        rows = response.xpath("//ul/li")
        items = []
        for row in rows:
            item = {}
            item['url'] = row.xpath("./a/@href").extract()
            item['name'] = row.xpath("./a/text()").extract()
            items.append(item)
        return items
        
        
        

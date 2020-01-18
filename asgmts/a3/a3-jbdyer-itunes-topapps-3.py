# Run with
#
# python -m scrapy runspider a3-jbdyer-itunes-topapps-3.py -t csv -o - > 3.csv

from scrapy import Request
from scrapy.spiders import Spider

class ItunesSpider(Spider):
    name = "itunes"
    handle_httpstatus_list = [404, 403]
    allowed_domains = ["apple.com"]
    start_urls = ["https://www.apple.com/uk/itunes/charts/free-apps/"]
    custom_settings = { 'DOWNLOAD_DELAY': 0.5 }
    
    def parse(self, response):
        '''
        This is run first and will scrape the main Itunes app page,
        then return a list of Request objects corresponding to the
        individual apps.
        '''
        apps = response.xpath("//section[@class='section apps chart-grid']//ul/li")
        ans = []
        for app in apps:
            item = {}
            
            # extract data
            item['app_name'] = app.xpath("./h3/a/text()").get()
            item['category'] = app.xpath("./h4/a/text()").get()
            item['appstore_link_url'] = app.xpath("./h3/a/@href").get()
            item['img_src_url'] = app.xpath("./a/img/@src").get()
            
            # now queue request objects
            url = item['appstore_link_url']
            req = Request(url, callback=self.parse_2)
            req.meta['x'] = item
            ans.append(req)
        return ans
    
    
    def parse_2(self, response):
        '''
        This parses the response from an individual app page and 
        adds information to the dictionary for that app.
        '''
        item = response.meta['x']
        
        item['star_rating'] = response.xpath("//span[@class='we-customer-ratings__averages__display']/text()").get()
        item['num_ratings'] = response.xpath("//div[@class='we-customer-ratings__count small-hide medium-show']/text()").get()
        return item
            

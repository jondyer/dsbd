# Run with
#
# python -m scrapy runspider a3-jbdyer-itunes-topapps-2.py -t csv -o - > 2.csv

from scrapy.spiders import Spider

class AppSpider(Spider):
    name = 'app_page'
    allowed_domains = ["apple.com"]
    start_urls = [ "https://apps.apple.com/gb/app/whatsapp-messenger/id310633997?v0=WWW-EUUK-ITSTOP100-FREEAPPS&l=en&ign-mpt=uo%3D4" ]
    
    def parse(self, response):
        item = {}
        item['star_rating'] = response.xpath("//span[@class='we-customer-ratings__averages__display']/text()").get()
        item['num_ratings'] = response.xpath("//div[@class='we-customer-ratings__count small-hide medium-show']/text()").get()
        return item
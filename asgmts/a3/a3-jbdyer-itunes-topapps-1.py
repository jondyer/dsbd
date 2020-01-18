# Run with
#
# python -m scrapy runspider a3-jbdyer-itunes-topapps-1.py -t csv -o - > 1.csv

from scrapy.spiders import Spider

class AppChartSpider(Spider):
    name = 'front_page'
    allowed_domains = ["apple.com"]
    start_urls = [ "https://www.apple.com/uk/itunes/charts/free-apps/" ]
    
    def parse(self, response):
        '''
        Scrapes the main app page to get name, category, link, and img url
        for each app. Returns a dict of this info.
        '''
        rows = response.xpath("//section[@class='section apps chart-grid']//ul/li")
        items = []
        for row in rows:
            item = {}
            item['app_name'] = row.xpath("./h3/a/text()").get()
            item['category'] = row.xpath("./h4/a/text()").get()
            item['appstore_link_url'] = row.xpath("./h3/a/@href").get()
            item['img_src_url'] = row.xpath("./a/img/@src").get()
            items.append(item)
        return items
        
        
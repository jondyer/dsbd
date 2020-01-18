# run with
# scrapy runspider s3.py -t csv -o - > o3.csv


from scrapy import Request
from scrapy.spiders import Spider

class S3(Spider):
    name = 's3'
    #allowed_domains
    base = "http://www.andrew.cmu.edu/~sraja/multi/"
    start_urls = [base+"main.html"]

    def parse(self, response):
        names = response.xpath('//ul/li')
        ans=[]
        for name in names:
            item = {}
            item['nickn'] = name.xpath('./a/text()').extract()
            url=item['url'] = name.xpath('./a/@href')[0].extract()
            req = Request(self.base+url, callback=self.parse_2)
            req.meta['x'] = item
#            ans.append(item)
            ans.append(req)            

#        print('******* %s' % ans)
        return ans

    def parse_2(self, response):
        item = response.meta['x']
        item['first'] = response.xpath('//li[@class="first"]/text()').extract()
        item['last'] = response.xpath('//li[@class="last"]/text()').extract()
        return item


#        /html/body/ul/li[1]/a



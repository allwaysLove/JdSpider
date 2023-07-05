import scrapy


class GoodsspiderSpider(scrapy.Spider):
    name = "goodsSpider"
    allowed_domains = ["jd.com"]
    start_urls = ["https://jd.com"]

    def parse(self, response):
        pass

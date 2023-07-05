import scrapy


class GoodsSpider(scrapy.Spider):
    name = "goods"
    allowed_domains = ["jd.com"]
    start_urls = ["https://jd.com"]

    def parse(self, response):
        pass

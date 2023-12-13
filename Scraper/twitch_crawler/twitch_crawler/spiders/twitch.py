import scrapy


class TwitchSpider(scrapy.Spider):
    name = "twitch"
    allowed_domains = ["www.twitch.tv"]
    start_urls = ["https://www.twitch.tv"]

    def parse(self, response):
        print(response.css('title::text').extract_first())
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import scraper_helper as sh


class TeamSpider(CrawlSpider):
    name = 'team'
    allowed_domains = ['example.com']  # TODO CHANGEME before run
    start_urls = ['https://www.example.com/team/']  # TODO CHANGEME before run

    rules = (
        Rule(LinkExtractor(allow=r'team/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        emails = sh.extract_emails(response.text)
        item = {
            'emails': emails,
            'url': response.url
        }
        return item

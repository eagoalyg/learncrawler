# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoz-odp.org']
    start_urls = [
        "https://dmoz-odp.org/Computers/Programming/Languages/Python/",
    ]


    def parse(self, response):
        for href in response.css("div.cat-item > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)


    def parse_dir_contents(self, response):
        for sel in response.xpath('//div[@class="results browse-content"]/div'):
            item = DmozItem()
            item['title'] = sel.xpath('div[@class="title-and-desc"]/a/div/text()').extract()[0]
            item['link'] = sel.xpath('div[@class="title-and-desc"]/a/@href').extract()[0]
            item['desc'] = sel.xpath('div[@class="title-and-desc"]/div/text()').extract()[0]
            yield item

#!/usr/bin/env python
#coding:utf-8
#
# Copy right (c) Addbook.cn
# Author:Yuan Lin
#
# Lisence: BSD

from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from urlparse import urljoin
from items import ScrapyCnItem
from scrapy import log
from scrapy.contrib.loader import ItemLoader

class AddbookSpider(Spider):
    """Crawl <book.douban.com>
       crawling only one page
       save data to db and json with utf-8
    """
    name = "onepage"
    base_domian = "book.douban.com"
    start_urls = (
            "http://book.douban.com/tag/Programming"
            )

    def parse(self, response):
        doc = Selector(response)
        item = ScrapyCnItem()
        sect = doc.xpath("//ul[@class='subject-list']/")
        for s in sect:
            title = s.xpath(".//li/div[@class='info']//a/@title").extract()
            href = s.xpath(".//li/div[@class='info']//a/@href").extract()
            img = s.xpath(".//li/div[@class='pic']//img/@src").extract()
            desc = s.xpath(".//li/div[@class='info']/p/text()").extract()
            item["title"] = [t.encode('utf-8') for t in title]
            item["img"] = [i.encode('utf-8') for i in img]
            item["desc"] = [d.encode('utf-8') for d in desc]
        return item

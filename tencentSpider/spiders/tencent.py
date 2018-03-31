# -*- coding: utf-8 -*-

import sys

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
 
from tencentSpider.items import TencentspiderItem

reload(sys)
sys.setdefaultencoding('utf-8')


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    pagelink = LinkExtractor(allow=("start=\d+"))
    rules = [
        Rule(pagelink, callback="parsetencent", follow=True)
    ]

    def parsetencent(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentspiderItem()
            item['position'] = each.xpath("./td[1]/a/text()").extract()[0]
            item['position_link'] = each.xpath("./td[1]/a/@href").extract()[0]
            item['position_type'] = each.xpath("./td[2]/text()").extract()[0]
            item['people_num'] = each.xpath("./td[3]/text()").extract()[0]
            item['work_location'] = each.xpath("./td[4]/text()").extract()[0]
            item['publish_time'] = each.xpath("./td[5]/text()").extract()[0]

            yield item

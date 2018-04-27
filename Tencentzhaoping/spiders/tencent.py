# -*- coding: utf-8 -*-
import scrapy,random,time
from Tencentzhaoping.items import TencentzhaopingItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=' + str(num) for num in range(0,3971,10)]

    def parse(self, response):
        """
        # 职位名称
        //tr[@class='even']/td/a/text()
        # 职位类别
        //tr[@class='even']/td[2]/text()
        # 人数
        //tr[@class='even']/td[3]/text()
        # 地点
        //tr[@class='even']/td[4]/text()
        # 发布时间
        //tr[@class='even']/td[5]/text()
        """
        # time.sleep(random.randint(1,3))
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentzhaopingItem()
            item['name'] = each.xpath("./td/a/text()").extract()[0]
            try:
                item['categroy'] = each.xpath("./td[2]/text()").extract()[0]
            except:
                item['categroy'] = ''
            try:
                item['people'] = each.xpath("./td[3]/text()").extract()[0]
            except:
                item['people'] = ''
            try:
                item['address'] = each.xpath("./td[4]/text()").extract()[0]
            except:
                item['address'] = ''
            try:
                item['datetime'] = each.xpath("./td[5]/text()").extract()[0]
            except:
                item['datetime'] = ''
            yield item
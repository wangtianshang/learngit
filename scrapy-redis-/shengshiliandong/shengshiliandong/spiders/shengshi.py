# -*- coding: utf-8 -*-
import scrapy
from ..items import ShengshiliandongItem
from scrapy_redis.spiders import RedisSpider

class ShengshiSpider(RedisSpider):
    name = 'shengshi'
    redis_key = "ShengshiSpider:start_urls"#必须要设置的一个Redis键
    # allowed_domains = ['shengshi.com']
    # start_urls = ['http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html']

    def parse(self, response):
        city1_list = response.xpath('//tr[@class="provincetr"]/td/a')
        for cityls in city1_list:
            city1 = cityls.xpath('./text()').extract_first()
            city1_href = cityls.xpath('./@href').extract_first()
            item = ShengshiliandongItem()
            item['first_city'] = city1
            if city1_href is not None:
                new_href = response.urljoin(city1_href)
                yield scrapy.Request(url=new_href,meta={'meta1':item},callback=self.city2)

    def city2(self,response):
        meta1 = response.meta['meta1']
        city2_list = response.xpath('//tr[@class="citytr"]/td[2]/a')
        for city2s in city2_list:
            city2 = city2s.xpath('./text()').extract_first()
            city2_href = city2s.xpath('./@href').extract_first()
            item = ShengshiliandongItem()
            item['first_city'] = meta1['first_city']
            item['second_city'] = city2
            if city2_href is not None:
                new_href = response.urljoin(city2_href)
                yield scrapy.Request(url=new_href, meta={'meta2': item}, callback=self.city3)

    def city3(self,response):
        meta2 = response.meta['meta2']
        city3_list = response.xpath('//tr[@class="countytr"]/td[2]/a')
        for city3s in city3_list:
            city3 = city3s.xpath('./text()').extract_first()
            city3_href = city3s.xpath('./@href').extract_first()
            item = ShengshiliandongItem()
            item['first_city'] = meta2['first_city']
            item['second_city'] = meta2['second_city']
            item['third_city'] = city3
            if city3_href is not None:
                new_href = response.urljoin(city3_href)
                yield scrapy.Request(url=new_href, meta={'meta3': item}, callback=self.city4)
    def city4(self,response):
        meta3 = response.meta['meta3']
        city4_list = response.xpath('//tr[@class="towntr"]/td[2]/a')
        for city4s in city4_list:
            city4 = city4s.xpath('./text()').extract_first()
            city4_href = city4s.xpath('./@href').extract_first()
            item = ShengshiliandongItem()
            item['first_city'] = meta3['first_city']
            item['second_city'] = meta3['second_city']
            item['third_city'] = meta3['third_city']
            item['fouth_city'] = city4
            if city4_href is not None:
                new_href = response.urljoin(city4_href)
                yield scrapy.Request(url=new_href, meta={'meta4': item}, callback=self.city5)
    def city5(self,response):
        meta4 = response.meta['meta4']
        city5_list = response.xpath('//tr[@class="villagetr"]/td[3]/text()').extract()
        for city5s in city5_list:
            item = ShengshiliandongItem()
            item['first_city'] = meta4['first_city']
            item['second_city'] = meta4['second_city']
            item['third_city'] = meta4['third_city']
            item['fouth_city'] = meta4['fouth_city']
            item['fifth_city'] = city5s
            yield item

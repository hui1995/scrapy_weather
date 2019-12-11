# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem
import re
import time
import json
class WeatherchinaSpider(scrapy.Spider):
    name = 'weatherchina'
    allowed_domains = ['nmc.cn']
    start_urls = ['http://www.nmc.cn/publish/forecast/china.html#']

    def parse(self, response):
        infolist=response.xpath('//div[@id="areaContent"]/div[@class="area"]/ul/li')
        for i in infolist:
            city=i.xpath('./div[@class="cname"]/a').xpath('string(.)').extract_first()
            href=i.xpath('./div[@class="cname"]/a/@href').extract_first()
            temperature=i.xpath('./div[@class="temp"]').xpath('string(.)').extract_first()
            temperature =temperature.split('/')
            maxTemperature=temperature[0].strip()+'℃'
            minTemperature=temperature[1].strip()
            weather=i.xpath('./div[@class="weather"]').xpath('string(.)').extract_first()
            item = WeatherItem()
            item['maxTemperature']=maxTemperature
            item['minTemperature']=minTemperature
            item['weather']=weather.strip()
            item['city']=city.strip()
            href='http://www.nmc.cn'+href
            request =scrapy.Request(href,callback=self.parseId,dont_filter=True)
            request.meta['item']=item
            yield request

    #
    def parseId(self,response):
        cityre = r"scode = '(.*?)';"  # 这是我们写的正则表达式规则，你现在可以不理解啥意思
        pattern1 = re.compile(cityre,re.S)  # 我们在编译这段正则表达式
        matcher1 = re.findall(pattern1, response.body.decode('utf8'))  # 在源文本中搜索符合正则表达式的部分
        cityid = matcher1[0]# 打印出来
        timestamp=str(int(time.time()*1000))
        url='http://www.nmc.cn/f/rest/real/'+cityid+'?_='+timestamp
        request=scrapy.Request(url,callback=self.parseContent,dont_filter=True)
        request.meta['item']=response.meta['item']
        yield request



    def parseContent(self,response):


        info=json.loads(response.body.decode('utf8'))
        weather=info['weather']
        humidity=weather['humidity']
        item =response.meta['item']
        item['humidity']=str(humidity)+'%'
        yield item


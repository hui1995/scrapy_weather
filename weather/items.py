# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city =scrapy.Field()
    weather=scrapy.Field()
    maxTemperature=scrapy.Field()
    minTemperature=scrapy.Field()
    humidity=scrapy.Field()

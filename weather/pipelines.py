# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook
import datetime
class WeatherPipeline(object):
    def process_item(self, item, spider):
        return item


class ExcelPipline(object):

    def __init__(self):

        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['城市', '天气', '最高温', '最低温度', '湿度',])
        self.date= (datetime.date.today()).strftime("%Y-%m-%d")

    def process_item(self,item,spider):
        line = [item['city'], item['weather'], item['maxTemperature'], item['minTemperature'], item['humidity'],
                ]
        self.ws.append(line)
        self.wb.save('./data/天气_'+str(self.date)+'.xlsx')
        return item


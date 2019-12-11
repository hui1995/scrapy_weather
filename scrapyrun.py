# _*_coding:utf-8_*_
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import schedule
import os
import datetime


def job():
    os.system('scrapy crawl weatherchina')
    date = (datetime.date.today()).strftime("%Y-%m-%d")

    smtp = smtplib.SMTP('smtp.qq.com')

    smtp.login('674837558@qq.com', 'zocmrdpgtacwbeda')
    imageFile = './data/天气_'+str(date)+'.xlsx'
    imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
    imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)
    m = MIMEMultipart()
    m.attach(imageApart)
    m['Subject'] = '天气信息'
    rev='674837558@qq.com'

    smtp.sendmail('674837558@qq.com',rev, m.as_string())

    smtp.quit()


if __name__ == '__main__':
    schedule.every().day.at('06:00').do(job)
    while True:
       schedule.run_pending()



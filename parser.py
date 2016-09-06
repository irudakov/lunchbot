# -*- coding: utf-8 -*-
import requests  
from lxml import html  
import sys  
# import urlparse
from urllib.parse import urlparse
from urllib.parse import urljoin

BASE_URL = 'http://paulaner-brauhaus.ru'
# BUSINES_LUNCH = unicode('Бизнес-ланч', "utf-8")
BUSINES_LUNCH = u'Бизнес-ланч'

def image_url():
   response = requests.get(BASE_URL + '/news/')
   parsed_body = html.fromstring(response.text.encode("utf-8"))

   titles = parsed_body.xpath('//h2/span/text()')
   links = parsed_body.xpath(u'//div[@class = "desc"][contains(./h2/span/text(), "Бизнес-ланч")]/a/@href')
#   links = [urlparse.urljoin(BASE_URL, url) for url in links]
   links = [urljoin(BASE_URL, url) for url in links]
#   print 'Found %s links' % len(links)

#   for link in links:
#       print link
   

#   for string in titles:
#      if BUSINES_LUNCH in string:
#          print string

   response_next = requests.get(links[0])
   parsed_body_next = html.fromstring(response_next.text)
   # Парсим ссылки с картинками
   image_links = parsed_body_next.xpath('//a[@class = "cbox npimage"]/@href')  
   if not image_links:  
        sys.exit("Found No Image links")
    
   # Конвертирование всех относительных ссылок в абсолютные
#   image_links = [urlparse.urljoin(response_next.url, url) for url in image_links]
   image_links = [urljoin(response_next.url, url) for url in image_links] 
#   print 'Found %s images' % len(image_links)
   return image_links[0]
   
   
# Скачиваем картинки
# for url in image_links:  
#     r = requests.get(url)
#     f = open('downloaded_images/%s' % url.encode().split('/')[-1], 'w')
#     f.write(r.content)
#     f.close()
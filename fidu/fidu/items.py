# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FiduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

	titulo = scrapy.Field()
	precio = scrapy.Field()
	numero_vendidos = scrapy.Field()
	envio_gratis = scrapy.Field()




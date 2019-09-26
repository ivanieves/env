import scrapy 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from fidu.items import FiduItem

class FiduSpider(CrawlSpider):
	name = 'fidu'
	item_count= 0
	allowed_domain = ['www.mercadolibre.com.co']
	start_urls= ['https://listado.mercadolibre.com.co/celulares#D[A:celulares]']

	rules = {

		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//span[@class="andes-pagination__arrow-title"]'))),
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//h2[@class="item__title list-view-item-title"]')),
							callback = 'parse_item', follow = False)
	
	} 

	def parse_item(self, response):
		ml_item = FiduItem()

		#info de los productos	
		ml_item['titulo'] = response.xpath('normalize-space(//*[@id="short-desc"]/div/header/h1/text())').extract()
		ml_item['precio'] = response.xpath('normalize-space(//*[@id="productInfo"]/fieldset[1]/span[2]/span[2]/text())').extract()
		ml_item['numero_vendidos'] = response.xpath('normalize-space(//div[@class="item-conditions"]/text())').extract()
		ml_item['envio_gratis'] = response.xpath('normalize-space(//*[@id="productInfo"]/div[1]/fieldset[2]/article/div[1]/p/span/text())').extract()
		self.item_count += 1
		if self.item_count >20:
			raise CloseSpider('item_exceeded')
		yield ml_item











import scrapy
from scrapy.http import FormRequest
from att.items import AttItem

class AttSpider(scrapy.Spider):
    name = 'att_spider'
    allowed_domains = ['tarifas.att.gob.bo']
    start_urls = ['https://tarifas.att.gob.bo/index.php/tarifaspizarra/tarifasInternetFijo']

    def parse(self, response):
        rows = response.xpath('//*[@id="kt_table"]/tbody/tr')
        for row in rows:
            item = AttItem()
            item['operador'] = row.xpath('.//td[1]/text()').get()
            item['departamento'] = row.xpath('.//td[2]/text()').get()
            item['nombre'] = row.xpath('.//td[3]/text()').get()
            item['velocidad_descarga'] = row.xpath('.//td[4]/text()').get()
            item['precio'] = row.xpath('.//td[5]/text()').get()
            item['tipo_instalacion'] = row.xpath('.//td[6]/text()').get()
            yield item
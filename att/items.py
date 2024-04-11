# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AttItem(scrapy.Item):
    operador = scrapy.Field()
    departamento = scrapy.Field()
    nombre = scrapy.Field()
    velocidad_descarga = scrapy.Field()
    velocidad_subida = scrapy.Field()
    precio = scrapy.Field()
    tipo_instalacion = scrapy.Field()

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImoveisItem(scrapy.Item):
    url = scrapy.Field()
    titulo = scrapy.Field()
    site = scrapy.Field()

    aluguel = scrapy.Field()
    condominio = scrapy.Field()
    iptu = scrapy.Field()
    aluguel_total = scrapy.Field()
    tipo_imovel = scrapy.Field()
    venda = scrapy.Field()

    descricao = scrapy.Field()
    endereco = scrapy.Field()
    logradouro = scrapy.Field()
    bairro = scrapy.Field()
    cidade = scrapy.Field()
    uf = scrapy.Field()

    area = scrapy.Field()
    vagas = scrapy.Field()
    quartos = scrapy.Field()
    suites = scrapy.Field()
    banheiros = scrapy.Field()

    imob_nome = scrapy.Field()
    imob_logo = scrapy.Field()
    imob_cod = scrapy.Field()
    imob_anunc = scrapy.Field()
    imob_tel = scrapy.Field()

    info_legais = scrapy.Field()

    imgs = scrapy.Field()

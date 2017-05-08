# -*- coding: utf-8 -*-
import scrapy
from imoveis.items import ImoveisItem
import re
import json

class VivarealSpider(scrapy.Spider):
    name = "vivareal"
    allowed_domains = ["vivareal.com.br"]
    start_urls = [
        #'https://www.vivareal.com.br/aluguel/sp/sao-paulo/',
        'https://www.vivareal.com.br/aluguel/sp/sao-paulo/?pagina=2'
    ]

    def parse(self, response):
        imoveis = ImoveisItem()

        for link in response.css('a.property-card__title::attr(href)').extract():
            link = 'https://www.vivareal.com.br' + link

            request = scrapy.Request(link, callback=self.handle_detail)
            request.meta["imoveis"] = imoveis
            yield request

    def handle_detail(self, response):
        imoveis = response.meta["imoveis"]
        # url = 'http://www.example.com'
        #
        # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36
        # Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FSL 7.0.6.01001)
        # Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0
        # Opera/9.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.01
        # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36
        # Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0
        #
        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
        # yield Request(url, headers=headers)
        # request = scrapy.Request(url, headers=headers)
        # fetch(request)

        #zap_json = response.css('body').re_first(r'application\/ld\+json\"\>(.*)\<\/script')
        #zap_img = response.css('.img-container img::attr(src)').extract()
        imgs_vivareal = response.css('.thumbs__item img::attr(data-src)').extract()

        json_vivareal = json.loads( response.css('.site-main__form-lead').re_first(r'data\-all\=.*(\{.*\}).*data\-recommendations') )#.replace("'",'"') 

        # telefone = list(set(response.css('a::attr(href)').re(r'tel\:(\d*)')))
        # #valores = response.css('.property-information--prices *::text').extract()
        # #response.css('.property-information__sub-price *::text').extract()
        # tipo_valores = response.css('.property-information__sub-price').re(r'title\"\>(\w+)')
        # valores = response.css('.property-information__sub-price').re(r'R\$\ (.*)\<\/dd')

        # imoveis['url'] = response.url
        # imoveis['titulo'] = response.css('span.property-title__name::text').extract_first()
        # imoveis['quartos'] = response.css('.icon-room > .property-information__item-description--expanded *::text').extract_first()
        # imoveis['suites'] = response.css('.icon-room > .property-information__item-description--expanded > .property-information__additional-info *::text').re_first(r'\(sendo (\d*) suíte\)')
        # imoveis['banheiros'] = response.css('.icon-bathroom > .property-information__item-description--expanded *::text').extract_first()
        # imoveis['vagas'] = response.css('.icon-garage > .property-information__item-description--expanded *::text').extract_first()
        # imoveis['area'] = response.css('.icon-area span.property-information__item-unit::text').extract_first()

        # imoveis['tipo_imovel'] = response.css('.icon-building dd.property-information__item-description::text').extract_first()
        # imoveis['venda'] = float( response.css('.icon-price span.property-information__item-unit::text').re_first(r'R\$ (.*)') )

        # imoveis['condominio'] = float( valores[tipo_valores.index('Condomínio')] )
        # imoveis['iptu'] = float( valores[tipo_valores.index('IPTU')] )
        # imoveis['aluguel_total'] = float( response.css('.property-information__item-unit--highlight::text').re_first(r'R\$\ (.*)') )#valores[valores.index('Valor com condomínio')+1]
        # imoveis['aluguel'] = imoveis['aluguel_total'] - imoveis['condominio']
        
        # imoveis['descricao'] = response.css('.property-description__detail *::text').extract_first()
        # imoveis['endereco'] = response.css('.touch-nav__address *::text').extract_first()
        # imoveis['logradouro'] = response.css('.map-location__address *::text').extract_first()
        # imoveis['bairro'] = response.css('.breadcrumb__item:last-child > span *::text').extract_first()
        # imoveis['uf'] = response.css('.breadcrumb__item:nth-child(3) *::attr(title)').extract_first()
        # imoveis['imob_tel'] = telefone
        # imoveis['imob_logo'] = response.css('.publisher__logo-container > a > img::attr(src)').extract_first()
        # imoveis['imob_anunc'] = response.css('.publisher__contact-info > strong:nth-child(1) *::text').extract_first()
        # imoveis['imob_cod'] = response.css('.publisher__contact-info > strong:nth-child(2) *::text').extract_first()
        # imoveis['info_legais'] = response.css('.legal-information__detail *::text').extract()


        #response.css('.legal-information__detail > p *::text').extract_first()
        yield json_vivareal
        # return imoveis
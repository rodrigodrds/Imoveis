# -*- coding: utf-8 -*-
import scrapy
from imoveis.items import ImoveisItem
import re
import json

class ZapimoveisSpider(scrapy.Spider):
    name = "zapimoveis"
    allowed_domains = ["zapimoveis.com.br"]
    start_urls = [
        #'https://www.zapimoveis.com.br/aluguel/imoveis/sp+sao-paulo/?pagina=1',
        'https://www.zapimoveis.com.br/aluguel/imoveis/sp+sao-paulo/?pagina=2'
    ]

    def start_requests(self):
        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)

    def parse(self, response):
        imoveis = ImoveisItem()

        for link in response.css('a.btn-ver-detalhes::attr(href)').extract():
            # self.log(link)
            # link = 'https://zapimoveis.com.br/' + link

            user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FSL 7.0.6.01001)', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0',
            'Opera/9.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.01', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0']

            headers = {'User-Agent': user_agent[0]}
            # self.log(user_agent[0])
            request = scrapy.Request(link, headers=headers, callback=self.handle_detail)
            request.meta["imoveis"] = imoveis
            yield request

    def handle_detail(self, response):
        #imoveis = response.meta["imoveis"]
        zap_json = json.loads( response.css('body').re_first(r'application\/ld\+json\"\>(.*)\<\/script') )
        self.log(len(zap_json))
        zap_img = response.css('.img-container img::attr(src)').extract()

        yield zap_json[-1]

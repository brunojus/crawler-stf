# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
import os
import re
import csv
from stf.items import JurisItem

class ProcessoSpider(scrapy.Spider):
    processos = []
    name = 'processo'
    allowed_domains = ['www.stf.jus.br']
    start_urls = ['http://www.stf.jus.br/portal/processo/listarProcesso.asp/']

    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver')  
    
    def start_requests(self):
        url = 'http://www.stf.jus.br/portal/processo/listarProcesso.asp'

        self.driver.get(url)

        #Mudar o parâmetro no sendKeys
        self.driver.find_element_by_id('numero').send_keys("AC 500")
        
        self.driver.find_element_by_css_selector('#dropmsgform > div:nth-child(7) > input[type="button"]:nth-child(2)').click()
      
        yield scrapy.Request(url, self.parse)

    def parse(self, response):        

        response = Selector(text=self.driver.page_source.encode('utf-8'))

        
        table = response.xpath('//*[@id="divImpressaoProcessos"]/div[2]/table//tr')

        #Retira o cabeçalho da tabela
        for data in table[1:]:
            item = JurisItem()            
            item['data'] = data.xpath('td[1]//text()').extract_first().encode('utf8')
            item['andamento'] = data.xpath('td[2]//text()').extract_first().encode('utf8')
            item['orgao_julgador'] = data.xpath('td[3]//text()').extract_first().encode('utf8')
            item['observacao'] = data.xpath('td[4]//text()').extract_first().encode('utf8')
            item['documento'] = data.xpath('td[5]//text()').extract_first().encode('utf8')

            yield item
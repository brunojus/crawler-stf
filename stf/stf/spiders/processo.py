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
from selenium.webdriver.support.select import Select
import logging
logger = logging.getLogger(__name__)

class ProcessoSpider(scrapy.Spider):
    processos = []
    name = 'processo'
    allowed_domains = ['www.stf.jus.br']
    start_urls = ['http://www.stf.jus.br/portal/processo/listarProcesso.asp/']

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.options.add_argument('window-size=1200x600')
        self.driver = webdriver.Chrome('chromedriver',chrome_options=self.options)  
        # self.driver = webdriver.Chrome('chromedriver')  
    
    def start_requests(self):
        url = 'http://stf.jus.br/'

        self.driver.get(url)

        #Mudar o parâmetro no sendKeys
        filterSelector = Select(self.driver.find_element_by_class_name('tipo-pesquisa-processo'))

        for option in filterSelector.options:
            if option.text == 'Por Número Único':
                option.click()

        processo = "00045021120040010000"
        for letter in processo:  
            time.sleep(0.01)          
            self.driver.find_element_by_id('pesquisaPrincipalNumeroUnico').send_keys(letter)
            time.sleep(0.1)
        
        self.driver.find_element_by_id('btnPesquisar').click()
      
        yield scrapy.Request(url, self.parse)

    def parse(self, response):        

        andamentos = self.driver.find_elements_by_class_name('andamento-detalhe')
        for andamento in andamentos: 
            item = JurisItem() 
            item['data'] = andamento.find_element_by_class_name('andamento-data').text
            item['andamento'] = andamento.find_element_by_class_name('andamento-nome').text
            item['observacao'] = andamento.find_elements_by_css_selector('div')[6].text

            yield item


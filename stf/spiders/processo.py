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
import MySQLdb
import MySQLdb.cursors

class ProcessoSpider(scrapy.Spider):
    name = 'processo'
    allowed_domains = ['www.stf.jus.br']
    start_urls = ['http://www.stf.jus.br/portal/processo/listarProcesso.asp/']

    def __init__(self,processo='', *args, **kwargs):
        super(ProcessoSpider, self).__init__(*args, **kwargs) 
        self.processo = processo
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.options.add_argument('window-size=1200x600')
        self.driver = webdriver.Chrome('chromedriver',chrome_options=self.options)  
        self.conn = MySQLdb.connect(user='root', passwd='121294', db='stf', host='127.0.0.1', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

        self.driver = webdriver.Chrome('chromedriver')  
    
    def start_requests(self):
        url = 'http://stf.jus.br/'

        self.driver.get(url)

        
        #Mudar o parâmetro no sendKeys
        filterSelector = Select(self.driver.find_element_by_class_name('tipo-pesquisa-processo'))

        for option in filterSelector.options:
            if option.text == 'Por Número Único':
                option.click()

        self.cursor.execute('SELECT numero_processo FROM processos')
        rows = self.cursor.fetchall()
        for row in rows:
            self.processo = row
            for letter in str(row):  
                time.sleep(0.1)          
                self.driver.find_element_by_id('pesquisaPrincipalNumeroUnico').send_keys(letter)
                time.sleep(0.1)
            self.driver.find_element_by_id('btnPesquisar').click()
            yield scrapy.Request(url, self.parse)
        self.cursor.close()          
      
    def parse(self, response):        

        andamentos = self.driver.find_elements_by_class_name('andamento-detalhe')
        for andamento in andamentos: 
            item = JurisItem() 
            item['data'] = andamento.find_element_by_class_name('andamento-data').text
            item['andamento'] = andamento.find_element_by_class_name('andamento-nome').text
            item['observacao'] = andamento.find_elements_by_css_selector('div')[6].text

            yield item


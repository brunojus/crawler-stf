# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
import os
import re

class ProcessoSpider(scrapy.Spider):
    name = 'processo'
    allowed_domains = ['www.stf.jus.br']
    start_urls = ['http://www.stf.jus.br/portal/processo/listarProcesso.asp/']

    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver')  

    def parse(self, response):
        self.driver.get('http://www.stf.jus.br/portal/processo/listarProcesso.asp')
        time.sleep(3)
        self.driver.find_element_by_id('numero').send_keys("AC 500")
        self.driver.find_element_by_css_selector('#dropmsgform > div:nth-child(7) > input[type="button"]:nth-child(2)').click()

        SMRtable = self.driver.find_element_by_xpath('//*[@id="divImpressaoProcessos"]/div[2]/table/tbody')

        for i in SMRtable.find_elements_by_xpath('.//tr'):
            print(i.get_attribute('innerHTML'))
        
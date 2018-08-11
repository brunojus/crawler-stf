from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import sys
import time
import os
import re
from pyvirtualdisplay import Display

# disp = True # True significa headless browser
# if disp:
#   display = Display(visible=0, size=(800, 600))
#   aux = display.start()
# # chromedriver = "chromedriver"
# # os.environ["webdriver.chrome.driver"] = chromedriver
# #driver = webdriver.Firefox()
# wait = ui.WebDriverWait(driver, 20)
# # time.sleep(3)

def pega_recurso(n_processo):
  driver = webdriver.Chrome('chromedriver')
  
  link = 'http://www.stf.jus.br/portal/processo/listarProcessoUnico.asp'
  driver.get(link)
  # driver.find_element_by_id('idNumeroProcesso').send_keys(recurso)
  driver.find_element_by_id('numero').send_keys(n_processo)
  driver.find_element_by_css_selector('#dropmsgform > div:nth-child(7) > input[type="button"]:nth-child(2)').click()

  time.sleep(3)
#   botao = "idBotaoFormularioExtendidoNovaConsulta"
#   #wait.until(lambda driver: len(driver.find_elements_by_id(botao)) > 0)
#   try:
#     time.sleep(1)
#     h = driver.find_element_by_id('idDivAbasConteudo').get_attribute('innerHTML')
#   except:
#     return 'erro'
#   h = h.encode('UTF-8')
#   if path != 'NAO':
#     f = open(path + '/' + n_processo + '.html', 'w')
#     f.write(h)
#     f.close()
#   return 'OK'

# def fecha():
#   driver.close()

pega_recurso('AC 500')
# fecha()
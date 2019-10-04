import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def seg():
	with open("urls.txt", "r") as url:
		for SearchString in url:
			try:
				browser = webdriver.Firefox()
				browser.get(('https://google.com'))
				SearchElem=browser.find_element_by_name('q')
				SearchElem.send_keys(SearchString)
				SearchButton = browser.find_element_by_xpath("//div[@class='FPdoLc VlcLAe']//input[@value='Google Search']")
				SearchButton.click()
				SearchElem=browser.find_element_by_xpath("//a[contains(text(),'Website')]")
				SearchElem.click()
			except:
				SearchElem=browser.find_element_by_class_name('LC20lb')
				SearchElem.click()

if __name__ == '__main__':
	seg()

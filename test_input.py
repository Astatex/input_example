from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestInput:
	def test_send_keys(self, open_browser):
		driver = open_browser
		driver.get('https://the-internet.herokuapp.com')
		elem_link = driver.find_element(By.LINK_TEXT, 'Form Authentication')
		elem_link.click()

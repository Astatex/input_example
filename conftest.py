import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture()
def open_browser():
	options = ChromeOptions()
	options.headless = True
	driver = webdriver.Chrome(options=options)
	yield driver
	driver.quit()
from dotenv import load_dotenv
from selenium import webdriver
import os

load_dotenv(override=True)

def pypi():
  browser = webdriver.Chrome()
  browser.get("http://python.org")

  menus = browser.find_elements_by_css_selector('#top ul.menu li')

  pypi = None
  for m in menus:
      if m.text == "PyPI":
          pypi = m
      print(m.text)

  pypi.click()

  browser.quit()



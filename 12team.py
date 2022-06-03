# -*- coding: utf-8 -*-
"""12team.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pmZPtndFt08sc76TFBHzhX1jSZs--UVe
"""

!pip install selenium
!apt-get update
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin

import sys
sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', options=chrome_options)

import selenium
from selenium import webdriver as wd
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests

import pandas as pd
from selenium import webdriver
import time
import math

import sys
import os
import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
from selenium import webdriver
import time
from tqdm import tqdm_notebook
import warnings ; warnings.filterwarnings(action='ignore')

url = 'https://www.coupang.com/'
driver.get(url)
time.sleep(3)

query_text = '에어팟프로'

element=driver.find_elements_by_css_selector('headerSearchKeyword')
element.send_keys(query_text)
element.submit()
time.sleep(1)

urls=driver.find_elements_by_css_selector(".search-product-link")
url_list=[]
for url in urls:
    url=url.get_attribute('href')
    url_list.append(url)
    
print(len(url_list))
url_list

tmp=pd.DataFrame({'url':url_list})
tmp.head(10)
tmp.to_excel('coupang_url_airpods.xlsx')
url_load=pd.read_excel("coupang_url_airpods.xlsx",engine='openpyxl')
num_list=len(url_load)
print(num_list)
url_load.head()
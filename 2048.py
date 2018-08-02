#! python3
# 2048.py - Program plays 2048 by sending up, right, down, left

from selenium import webdriver
import random

browser = browser = webdriver.Firefox(executable_path=r'C:\\Anaconda3\\selenium\\webdriver\\firefox\\geckodriver.exe') 
browser.get('https://gabrielecirulli.github.io/2048/')

moves = {'1': 'Keys.UP', '2': 'Keys.RIGHT', '3': 'Keys.DOWN', '4':'Keys.LEFT'}



while True:
	browser.implicitly_wait(2)
	move = random.randint(1, 4)
	
	htmlElem = browser.find_element_by_tag_name('html')
	htmlElem.send_keys(moves.get(str(move)))

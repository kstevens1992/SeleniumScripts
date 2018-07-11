#!/usr/bin/python3
# download searched photos on 500px

import time, requests, os
from selenium import webdriver
from selenium.webdriver.common.by import By

def downloadPageImage(broswer, imageNum):
	# find the source of the comic image 
		photoElement = broswer.find_element(By.CLASS_NAME, 'photo')
		photoURL = photoElement.get_attribute('src')
		print(photoURL)
		res = requests.get(photoURL)
		res.raise_for_status()

		# save the image to folder
		imageFile = open(os.path.join('500px', str(imageNum)) + '.png', 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()
		
		# get the prevous button URL
		nextLink = browser.find_elements(By.CSS_SELECTOR, 'div.nav:nth-child(5) > div:nth-child(1)')
		nextLink[0].click()



os.makedirs('500px', exist_ok=True)

searchText = input('What would you like to search for? ')
downloadAmount = int(input('How many would you like to download? '))

browser = webdriver.Firefox()
browser.get('https://500px.com/search?submit=Submit&q={}&type=photos'.format(searchText))

firstImage = browser.find_elements(By.XPATH,'/html/body/div[4]/div/div[1]/div[3]/div/div/div/div/div[1]/a')
firstImage[0].click() # click on first image 
time.sleep(3)

for imageNum in range(downloadAmount):
	downloadPageImage(browser, imageNum)
	time.sleep(3)

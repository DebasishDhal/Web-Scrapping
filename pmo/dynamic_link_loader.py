#The news page of PMO is dynamically loaded. I want to get as many news links as possible, so this code scrolls down for as long as you want (Given you wait accordingly)

main_pmo_url = 'https://www.pmindia.gov.in/ory/%e0%ac%b8%e0%ac%a6%e0%ad%8d%e0%ad%9f%e0%ac%a4%e0%ac%ae-%e0%ac%96%e0%ac%ac%e0%ac%b0/'

from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
driver.get(main_pmo_url)

def scroll_to_bottom(wait_time):
    # scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(wait_time)  # Add a short delay to allow content to load

for i in range(1000):
    waiting_time = min(5+i/10,15) #15 sec is optimal. Using this, I scrolled down 1000 times. If the content doesn't load within the waiting time even once, you gotta start over.
    scroll_to_bottom(waiting_time)
    print(f'scroll count = {i}, wait = {waiting_time:.2f}', end='\r')

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

links = []
for i in soup.find_all('div', class_='news-description'): #To get the links of the news articles in PMO website. This gave me news from 2023 to 2017.
    link = i.find('a')['href']
    if '/ory/' in link:
        links.append(link)

links = list(set(links)) #Avoiding duplication just in case. This ruins ordering of links.

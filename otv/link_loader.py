#This gives you all the links of a particular theme (national-news, sports, information etc.) from OTV website.
#You pick the topic and change the main_url in for loop accordingly. Then enter the upper limit of page for that topic.

import requests
from bs4 import BeautifulSoup

upper_limit = 33300 #National
exception_count = 0
context_specific_links = []
interrupted = False
for i in range(25, upper_limit, 25):
    if i%500==0:
        print('Fetched', i, ' pages', end = '\r')
    try:
        main_url = 'https://otvkhabar.in/national/'+str(i) #
        main_soup = BeautifulSoup(requests.get(main_url).text, 'html.parser')
        link_divs = main_soup.find_all('div', class_='listing-result-news')
        #Links are stored as href under tag a
        link_list = [link_div.find('a')['href'] for link_div in link_divs]
        context_specific_links.extend(link_list)
    except KeyboardInterrupt:
        interrupted = True
        break        
    except:
        print('Some error occured while fetching ', main_url)

assert interrupted is False, 'Interrupted by user'

context_specific_links =  [link.strip() for link in context_specific_links if 'https://otvkhabar.in/' in link]
print('Total context links fetched : ', len(context_specific_links))
context_specific_links = '\n'.join(context_specific_links)

with open(r'Your_adress', 'w') as f:
    f.write(context_specific_links)

from bs4 import BeautifulSoup
import requests
from otv_single_article_scrapper import main

#We go one link after another. If the article is scrapped, we add it to our list of links that have been scrapped.
with open('Adress of collection of links that are to be scrapped', 'r', encoding = 'utf-8') as f:
  links_to_scrap = f.read().split('\n')  

with open('Adress of collection of links that have already been scrapped', 'r', encoding = 'utf-8') as f:
  scrapped_links_global = f.read().strip().split('\n')
  scrapped_links_global = [item for item in scrapped_links_global if item != '']

with open('Adress of your combined scrapped text', 'r', encoding = 'utf-8') as f:
  existing_text = f.read()

# links_to_scrap = [link for link in links_to_scrap if link not in scrapped_links_global]
print('Session begins: -')
print(f'Links already scrapped = {len(scrapped_links_global)}')

links_visited = 0
head_start = 0 #If you want to start from a particular index, to save time.

links_visited += head_start
for link in links_to_scrap[head_start:]:
  links_visited += 1

  with open('Adress of collection of links that have already been scrapped', 'r', encoding = 'utf-8') as f:
    scrapped_links_global = f.read().split('\n')

  if link in scrapped_links_global:
    continue

  with open('Adress of your combined scrapped text', 'r', encoding = 'utf-8') as full_content:
    existing_text = full_content.read()

  new_text = main(link)

  if new_text is None:
    print('content is None', end = '\r')
    continue
  
  existing_text = existing_text + '\n' + new_text
  scrapped_links_global.append(link)
  print( f"Links visited={links_visited:,}, Tokens collected={len(existing_text.split()):,}, Sentence count = {existing_text.count('।'):,} , Links scrapped = {len(scrapped_links_global):,}") 

  scrapped_links_global = '\n'.join(scrapped_links_global).strip()

  with open('Adress of collection of links that have already been scrapped', 'w', encoding = 'utf-8') as full_content:
    full_content.write(existing_text.strip())
  
  with open('Adress of your combined scrapped text', 'w', encoding = 'utf-8') as scrapped:
    scrapped.write(scrapped_links_global)

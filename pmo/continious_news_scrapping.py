#So, I got a large list of links to scrap from. This script tries to scrap all the links from that list.

import requests
from bs4 import BeautifulSoup
from pmo_single_publication_scrapper import content_extractor, date_extractor, title_extractor

links_to_scrap_adress = 'Adress where you store the links to scrap'
with open(links_to_scrap_adress, 'r') as f:
    scrapped_links_global = f.read().strip().split('\n')
    scrapped_links_global = [item for item in scrapped_links_global if item != '']

scrapped_data_adress = 'Adress where your scrapped data from PMO website is stored'
with open(scrapped_data_adress, 'r', encoding = 'utf-8') as existing:
    existing_text = existing.read()

scrapped_link_adress = 'Adress where all the already scrapped links are stored'
with open(scrapped_link_adress, 'r') as f:
    links_to_scrap = f.read().split('\n')

links_to_scrap = [link for link in links_to_scrap if link not in scrapped_links_global] 

batch_text = '' 
count = len(scrapped_links_global)

for link in links_to_scrap:
    with open('/content/gdrive/MyDrive/ACL2024/Data/pmo_odia_created/pmo_all_dumped.txt', 'r', encoding = 'utf-8') as existing:
        existing_text = existing.read()

    with open('/content/gdrive/MyDrive/ACL2024/Data/pmo_odia_created/pmo_link_scrapped.txt', 'r') as f:
        scrapped_links_global = f.read().split('\n')

    if link in scrapped_links_global:
        continue

    print(link.strip())
    if 'https://www.pmindia.gov.in/ory/news_updates/' not in link: #ensure that the content is in Odia
        continue
    try:
        response = requests.get(link.strip(), timeout=10)
        response.raise_for_status()  # Raise an error for bad responses (e.g., 404, 500)
        soup = BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.Timeout:
        print(f"Request for {link} timed out after 10 seconds. Skipping.")
        continue
    except requests.exceptions.RequestException as e:
        print(f"Error while requesting {link}: {e}")
        continue    

    title = title_extractor(soup)    
    date = date_extractor(soup)
    content = content_extractor(soup)
    if content == '':
        print('Content not scrapped')
        continue
    if title != '':title = 'ଶୀର୍ଷକ : ' + title

    date = 'ତାରିଖ : ' + date
    
    main_content = (title + '\n' + date + '\n' + content).replace('।\n”','।”\n').replace("।\n’","।’\n").strip()
    batch_text += main_content
    # print(main_content)
    count += 1

    existing_text = (existing_text + '\n' + main_content).strip()
    scrapped_links_global.append(link)
    scrapped_links_global = '\n'.join(scrapped_links_global).strip()

    print(f"Existing token count = {len(existing_text.split())}, Date = {date}")

    with open('/content/gdrive/MyDrive/ACL2024/Data/pmo_odia_created/pmo_all_dumped.txt', 'w', encoding = 'utf-8') as new:
        new.write(existing_text)
    with open('/content/gdrive/MyDrive/ACL2024/Data/pmo_odia_created/pmo_link_scrapped.txt', 'w') as new:
        new.write(scrapped_links_global)

    print(count, end = '\n\n')

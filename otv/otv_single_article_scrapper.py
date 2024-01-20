import requests
from bs4 import BeautifulSoup

def title_extractor(soup):
    try:
        return soup.find('div', class_ = 'article-info').find('h1').text.strip()
    except:
        return None
    
def content_extractor(soup):
    try:
        article_content_ptags = soup.find('div', class_='article-content').find_all('p')
        article_content = ''
        for ptag in article_content_ptags:
            try:
                article_content += '\n'+ptag.text.strip()
            except:
                pass
        return article_content.strip()
    except:
        return None

def main(url):
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    title = title_extractor(soup)
    single_content_only = content_extractor(soup)

    if title is None or single_content_only is None:
        return None
    forbideen_chars = ['#', '.com', '.in', 'https://', '@otv']
    single_content = ('ଶୀର୍ଷକ : ' + title+'\n' + single_content_only).replace('।','।\n').replace('\n”','”\n').replace("\n’", '’\n')
    single_content = single_content.split('\n')
    single_content = [item for item in single_content if any([char in item for char in forbideen_chars])==False]
    single_content = '\n'.join( [item.strip() for item in single_content if ( len(set(item))>=2 )] )
    return single_content.strip()

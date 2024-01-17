from bs4 import BeautifulSoup
import re, requests, string

def filter_span_and_p(tag):
    if tag.name == 'span' and 'style' in tag.attrs and tag['style'] in [',sans-serif', ',serif', 'font-family:Mangal']:
        # To get those tags who have string directly under them, this is to avoid duplication.
        if tag.string:
            return True
    elif tag.name == 'p' and 'style' in tag.attrs and tag['style'] in ['text-align:justify', 'text-align: justify;']:        
        if tag.string:
            return True
    return False

def content_extractor(soup):
    found_elements = soup.find_all(filter_span_and_p)
    content = ''
    added_text = []
    for i in found_elements:
        text = i.get_text(strip=True)
        if len(text) > 20 and text.strip() in added_text:
            continue
        content += text + ' '
        added_text.append(text)

    words = [word.strip() for word in content.split() if 1<=len(word)<=50]
    content = ' '.join(words)
    content = content.replace(' ,', ',').replace(' .', '.').replace('\u200c', '')
    content = re.sub(r'\s+–\s+', '–', content.strip())
    content = re.sub(r' ।(.)', r' ।\1\n', content) #To accomodate for sentences like random_text ।" (I don't want the just quotation mark to be in the next line)
    content = content.replace('। ', ' । ').replace(' । ', ' ।\n').replace('  ।', ' ।').replace('*','')

    #Remove empty lines
    content = '\n'.join([line.strip() for line in content.split('\n') if len(line.strip()) > 0])

    #Do linewise de-duplication
    lines = content.split('\n')
    content = ''
    for line in lines:
        if all(char in set(string.ascii_uppercase + string.punctuation + ' '+ '\u200b') for char in set(line)):
            continue
        if len(line.strip()) == 0:
            continue
        if line not in content:
            content += line + '\n'

    #Content often has initials of the writer at the end of the article. It consists of just capital letters and maybe one space. Remove them
    content = re.sub(r'\n[A-Z ]+$', '', content)
    content = re.sub(r'\b[A-Z]+\s*$', '', content.strip())
    content = re.sub(r'\b[A-Z]+\s*$', '', content)
    content = re.sub(r'https?://\S+', '', content) #Remove links
    return content

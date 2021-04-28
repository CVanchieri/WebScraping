### This is a webscraper that pulls blog posts from www.datasciencecentral.com ### 
# beautifulsoup4 - latest version
# parser used - lxml 
# requests library 

from bs4 import BeautifulSoup
import requests

### html file ### 
# with open('simple.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

# match = soup.title.text # .text to show only text no tags 
# print(match) # prettify to show indentations
# print('----')
# # article = soup.find('div', class_='article') # search for div that includes 'article', 1st match 
# for article in soup.find_all('div', class_='article'): # search for div that includes 'article', returns list of all matches 

#     headline = article.h2.a.text 
#     print(headline)
#     summary = article.p.text
#     print(summary)
#     print('----')

### html webpage ### 
source =requests.get('https://www.datasciencecentral.com').text
soup = BeautifulSoup(source, 'lxml')
article = soup.find('div', class_='xg_module module_blog indented_content')
title = article.h2.text
print('-Title-')
print(title)
print('---')
#print(article.prettify())
for post in soup.find_all('div', class_='blogpost vcard'):
    author_image = post.div.span.a.span.img['src']
    author_name = post.p.a.text
    header_text = post.h3.a.text
    
    print('#######-Blog Post-#######')
    print('-Content Author Image-')
    print(author_image)
    print('-Content Author Name-')
    print(author_name)
    print('-Content Header Text-')
    print(header_text)
    print('-Content Body Image-')
    try:
        if post.find('img', class_=['align-full']) is not None:
            print(post.find('img', class_=['align-full'])['src'])
    except Exception as e:
        print('None')

    print('-Content Body Text-')
    body = post.find('div', class_='xg_user_generated')
    try:
        if body.select_one('.xg_user_generated li:nth-child(1)').text != '':
            print(body.select_one('.xg_user_generated li:nth-child(1)').text)
    except Exception as e:
        pass  
    try:
        if body.select_one('.xg_user_generated li:nth-child(2)').text != '':
            print(body.select_one('.xg_user_generated li:nth-child(2)').text)
    except Exception as e:
        pass  
    try:
        if body.select_one('.xg_user_generated p:nth-child(2)').text != '':
            print(body.select_one('.xg_user_generated p:nth-child(2)').text)
    except Exception as e:
        pass   
    try:
        if body.select_one('.xg_user_generated p:nth-child(3)').text != '':
            print(body.select_one('.xg_user_generated p:nth-child(3)').text)
    except Exception as e:
        pass
    try:
        if body.select_one('.xg_user_generated p:nth-child(4)').text != '':
            print(body.select_one('.xg_user_generated p:nth-child(4)').text)
    except Exception as e:
        pass
    print('-Contenet Link-')
    try:
        if body.find('a', class_=['xj_expandable'])['href'] is not None:
            print(body.find('a', class_=['xj_expandable'])['href'])
    except Exception as e:
        pass




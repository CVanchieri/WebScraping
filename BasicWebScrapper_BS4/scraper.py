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

    print('-Author Image-')
    print(author_image)
    print('-Header Text-')
    print(header_text)
    print('-Author-')
    print(author_name)
    body = post.find('div', class_='xg_user_generated')
    body_text1 = body.select_one('.xg_user_generated p:nth-child(2)')
    body_text2 = body.select_one('.xg_user_generated p:nth-child(3)')
    print('-Body Text-')
    print(body_text1)
    print(body_text2)
    print('---')



# for article in soup.find_all('h3', class_='title'): # search for div that includes 'article', returns list of all matches 

#     headline = article.a.text
#     print(headline)



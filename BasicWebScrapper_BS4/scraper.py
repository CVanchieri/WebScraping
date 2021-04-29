### This is a webscraper that pulls blog posts from www.datasciencecentral.com ### 
# beautifulsoup4 - latest version
# parser used - lxml 
# requests library 

from bs4 import BeautifulSoup
import requests
import csv 

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

csv_file = open('blog_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['author_image', 'author_name', 'header_text', 'body_text', 'content_link'])

for post in soup.find_all('div', class_='blogpost vcard'):
    author_image = post.div.span.a.span.img['src']
    author_name = post.p.a.text
    header_text = post.h3.a.text
    body = post.find('div', class_='xg_user_generated')
    body_text = ''
    content_link = ''
    
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
    try:
        if body.select_one('.xg_user_generated li:nth-child(1)').text != '':
            body1 = body.select_one('.xg_user_generated li:nth-child(1)').text
            body_text = body1
            print(body1)
    except Exception as e:
        body1 = '' 
        body_text = body1
    try:
        if body.select_one('.xg_user_generated li:nth-child(2)').text != '':
            body2 = body.select_one('.xg_user_generated li:nth-child(2)').text
            body_text = body1 + body2
            print(body2)
    except Exception as e:
        body2 = ''  
        body_text = body1 + body2
    try:
        if body.select_one('.xg_user_generated p:nth-child(2)').text != '':
            body3 = body.select_one('.xg_user_generated p:nth-child(2)').text
            body_text = body1 + body2 + body3
            print(body3)
    except Exception as e:
        body3 = ''
        body_text = body1 + body2 + body3   
    try:
        if body.select_one('.xg_user_generated p:nth-child(3)').text != '':
            body4 = body.select_one('.xg_user_generated p:nth-child(3)').text
            body_text = body1 + body2 + body3 + body4
            print(body4)
    except Exception as e:
        body4 = ''
        body_text = body1 + body2 + body3 + body4
    try:
        if body.select_one('.xg_user_generated p:nth-child(4)').text != '':
            body5 = body.select_one('.xg_user_generated p:nth-child(4)').text
            body_text = body1 + body2 + body3 + body4 + body5
            print(body5)
    except Exception as e:
        body5 = ''
        body_text = body1 + body2 + body3 + body4 + body5
    print('-Contenet Link-')
    try:
        if body.find('a', class_=['xj_expandable'])['href'] is not None:
            content_link = body.find('a', class_=['xj_expandable'])['href']
            print(content_link)
    except Exception as e:
        print('None')

    if body_text == '':
        body_text = ' None'

    csv_writer.writerow([author_image, author_name, header_text, body_text, content_link])

csv_file.close()


#!/usr/bin/env python
# coding: utf-8

# # Mission To Mars

# In[1]:


from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
import requests
import pymongo


# In[2]:


#create path 

executable_path = {"executable_path":"/Users/brittanyaylia/Desktop/chromedriver"}


# In[3]:


browser = Browser("chrome", **executable_path, headless=False)


# ## NASA Mars News

# In[4]:


#scrape mars news site

news_url = 'https://mars.nasa.gov/news/'
browser.visit(news_url)

html = browser.html
bsoup = bs(html, 'html.parser')


# In[5]:


#collect the latest news title and paragraph text

titles = bsoup.find('div', class_='content_title').text
print(titles)

paragraphs = bsoup.find('div', class_='article_teaser_body').text
print(paragraphs)


# ## JPL Mars Space Images 

# In[6]:


#find the image url for the current featured mars image

img_url = 'https://spaceimages-mars.com/'
browser.visit(img_url)

img_html = browser.html
bsoup = bs(img_html, 'html.parser')

featured = bsoup.find("img", class_='fade-in').get('src')
featured_url = f'https://spaceimages-mars.com/{featured}'
print(featured_url)


# ## Mars Facts

# In[7]:


#scrape the table containing facts about mars including diameter, mass, etc.

fax_url = "https://galaxyfacts-mars.com/"
browser.visit(fax_url)

fax_data = pd.read_html(fax_url)
fax_data = pd.DataFrame(fax_data[0])

mars_fax = fax_data.to_html(header= False, index = False)
print(mars_fax)


# ## Mars Hemispheres 

# In[21]:


#obtain urls and titles for high resolution images of mars hemispheres

hemi_url = 'https://marshemispheres.com/'
browser.visit(hemi_url)

html = browser.html
bsoup = bs(html, 'html.parser')

items = bsoup.find_all('div', class_='item')
images = []

for item in items:
    title = item.find('h3').text
    print(title)
    item_url = hemi_url + item.find('a')['href']
    
    browser.visit(item_url)
    html = browser.html
    bsoup = bs(html, 'html.parser')
    
    image_url = hemi_url + bsoup.find('img', class_='wide-image').get('src')
    print(image_url)
    
    insert = dict({"Title": title, "url": image_url})
    images.append(insert)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Mission To Mars

from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
import requests
import pymongo

def init_browser():
    executable_path = {"executable_path":"/Users/brittanyaylia/Desktop/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

mars_info = {}

def news(browser):
    browser = init_browser()

    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    html = browser.html
    bsoup = bs(html, 'html.parser')

    titles = bsoup.find('div', class_='content_title').text
    paragraphs = bsoup.find('div', class_='article_teaser_body').text

    mars_info['titles'] = titles.text
    mars_info['paragraphs'] = paragraphs.text

    browser.quit()
    return mars_info


def featured_image(browser):
    browser = init_browser()

    img_url = 'https://spaceimages-mars.com/'
    browser.visit(img_url)
    img_html = browser.html
    bsoup = bs(img_html, 'html.parser')

    featured = bsoup.find("img", class_='fade-in').get('src')
    featured_url = f'https://spaceimages-mars.com/{featured}'
    featured_url

    mars_info['featured_url'] = featured_url

    browser.quit()
    return mars_info


def mars_facts(browser):
    browser = init_browser

    fax_url = "https://galaxyfacts-mars.com/"
    browser.visit(fax_url)
    
    fax_data = pd.read_html(fax_url)
    fax_data = pd.DataFrame(fax_data[0])
    
    mars_fax = fax_data.to_html(header= False, index = False)
    mars_info['mars_facts'] = mars_fax

    browser.quit()
    return mars_info


def hemispheres(browser):
    browser = init_browser()
    
    hemi_url = 'https://marshemispheres.com/'
    browser.visit(hemi_url)
    html = browser.html
    bsoup = bs(html, 'html.parser')
    
    items = bsoup.find_all('div', class_='item')
    images = []

    for item in items:
        title = item.find('h3').text
        item_url = hemi_url + item.find('a')['href']
        
        browser.visit(item_url)
        html = browser.html
        bsoup = bs(html, 'html.parser')
        
        image_url = hemi_url + bsoup.find('img', class_='wide-image').get('src')
        
        insert = dict({"Title": title, "url": image_url})
        images.append(insert)

    mars_info['hemisphere_images'] = images

    browser.quit()
    return mars_info



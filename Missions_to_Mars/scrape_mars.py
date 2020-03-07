from splinter import Browser
from bs4 import BeautifulSoup as bs
import os
import pandas as pd
import time
import requests
import pymongo

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

def init_browser(): 
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape_mars_news():
    browser = init_browser()

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    browser.visit(url)
    html = browser.html

    soup = bs(html, 'html.parser')
    element = soup.select_one('ul.item_list li.slide')
    title = element.find("div", class_="content_title").get_text()

    news_title = element.find("div", class_="content_title").get_text()
    news_paragraph = soup.find("div", class_="article_teaser_body").get_text()

    mars_news_data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph
    }

    browser.quit()
    return mars_news_data

def featured_image():
    browser = init_browser()

    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    browser.click_link_by_id('full_image')

    html = browser.html
    image_soup = bs(html, "lxml")
    img_url = image_soup.find('img', class_ = 'fancybox-image')['src']

    featured_img_url = "https://www.jpl.nasa.gov" + img_url

    featured['featured_image_url'] = featured_image_url 

    browser.quit()
    return featured

def mars_facts():
    browser = init_browser

    url = "https://space-facts.com/mars/"
    browser.visit(url)

    facts = pd.read_html(url)

    facts_df = facts[0]
    facts_df.columns = ['Item', 'Value']

    html_table = facts_df.to_html()
    html_table.replace('\n', '') 

    mars_facts['html_table'] = html_table

    browser.quit()
    return mars_facts
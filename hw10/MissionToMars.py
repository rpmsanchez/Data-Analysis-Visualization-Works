#!/usr/bin/env python
# coding: utf-8

# In[85]:


from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
import pymongo
from splinter import Browser


# In[22]:


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# In[23]:


db = client.nasa_db
collection = db.articles


# In[24]:


# URL of page to be scraped
url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

# Retrieve page with the requests module
response = requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
soup = BeautifulSoup(response.text, 'lxml')
soup


# In[80]:


results = soup.find_all('div', class_="content_title")

for result in results:
    newstitle = result.find('a').text
    break


# In[81]:


results2 = soup.find_all('div', class_="image_and_description_container")
results2

for result in results2:   
    newspar = result.find('div', class_="rollover_description_inner").text
    break


# In[82]:


# LATEST ARTICLE TITLE AND PARAGRAPH

print(newstitle)
print(newspar)


# In[84]:





# In[88]:


get_ipython().system('which chromedriver')


# In[90]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[92]:


url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url2)


# In[101]:


# Retrieve page with the requests module
response2 = requests.get(url2)
# Create BeautifulSoup object; parse with 'lxml'
soup2 = BeautifulSoup(response2.text, 'lxml')
soup2


# In[127]:


results3 = soup2.find_all('div', class_="carousel_items")
#results3
for result in results3:
    words = result.find('article')
    text = words['style']
    text = text.split("(")
    text = text[1].replace(');',"").replace("'","")
    break
featured_image_url = "https://www.jpl.nasa.gov" + text


# In[145]:


# FEATURED IMAGE URL

featured_image_url


# In[188]:


# URL of page to be scraped
url7 = 'https://twitter.com/marswxreport?lang=en'
# Retrieve page with the requests module
response7 = requests.get(url7)
# Create BeautifulSoup object; parse with 'lxml'
soup7 = BeautifulSoup(response7.text, 'lxml')
soup7


# In[197]:


results7 = soup7.find('div', class_="js-tweet-text-container")

for result in results7:
    weather = results7.find('p').text

weather = weather.replace('\n', '')
weather


# In[130]:


url3 = 'https://space-facts.com/mars/'
tables = pd.read_html(url3)
tables


# In[131]:


df = tables[0]
df


# In[132]:


html_table = df.to_html()
html_table


# In[133]:


html_table.replace('\n', '')


# In[134]:


df.to_html('table.html')


# In[211]:


# URL of page to be scraped
url4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
# Retrieve page with the requests module
response3 = requests.get(url4)
# Create BeautifulSoup object; parse with 'lxml'
soup3 = BeautifulSoup(response3.text, 'lxml')


# In[212]:


results4 = soup3.find_all('img', class_="wide-image")
results4
for result in results4:
    img1 = result['src']

img1 = "https://astrogeology.usgs.gov" + img1

results4 = soup3.find_all('div', class_="content")
results4
for result in results4:
    hem1 = result.find("h2", class_='title').text
    
hem1 = hem1.replace(" Enhanced", "")
dic1 = {}
dic1["title"] = hem1
dic1["img_url"] = img1
dic1


# In[213]:


# URL of page to be scraped
url4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
# Retrieve page with the requests module
response3 = requests.get(url4)
# Create BeautifulSoup object; parse with 'lxml'
soup3 = BeautifulSoup(response3.text, 'lxml')


# In[214]:


results4 = soup3.find_all('img', class_="wide-image")
results4
for result in results4:
    img2 = result['src']

img2 = "https://astrogeology.usgs.gov" + img2

results4 = soup3.find_all('div', class_="content")
results4
for result in results4:
    hem2 = result.find("h2", class_='title').text
    
hem2 = hem2.replace(" Enhanced", "")
dic2 = {}
dic2["title"] = hem2
dic2["img_url"] = img2
dic2


# In[215]:


# URL of page to be scraped
url4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
# Retrieve page with the requests module
response3 = requests.get(url4)
# Create BeautifulSoup object; parse with 'lxml'
soup3 = BeautifulSoup(response3.text, 'lxml')


# In[216]:


results4 = soup3.find_all('img', class_="wide-image")
results4
for result in results4:
    img3 = result['src']

img3 = "https://astrogeology.usgs.gov" + img3

results4 = soup3.find_all('div', class_="content")
results4
for result in results4:
    hem3 = result.find("h2", class_='title').text
    
hem3 = hem3.replace(" Enhanced", "")
dic3 = {}
dic3["title"] = hem3
dic3["img_url"] = img3
dic3


# In[217]:


# URL of page to be scraped
url4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
# Retrieve page with the requests module
response3 = requests.get(url4)
# Create BeautifulSoup object; parse with 'lxml'
soup3 = BeautifulSoup(response3.text, 'lxml')


# In[218]:


results4 = soup3.find_all('img', class_="wide-image")
results4
for result in results4:
    img4 = result['src']

img4 = "https://astrogeology.usgs.gov" + img3

results4 = soup3.find_all('div', class_="content")
results4
for result in results4:
    hem4 = result.find("h2", class_='title').text
    
hem4 = hem4.replace(" Enhanced", "")
dic4 = {}
dic4["title"] = hem4
dic4["img_url"] = img4
dic4


# In[219]:


# LIST OF HEMISPHERE DICTIONARIES

hemisphere_image_urls = [dic1, dic2, dic3, dic4]
hemisphere_image_urls


# In[ ]:





# In[ ]:





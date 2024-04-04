#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[4]:


from bs4 import BeautifulSoup


# In[5]:


res = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(res.text,'html.parser')


# In[8]:


print(soup.find('span',class_ = 'text').text[1:-1])


# In[7]:





# In[11]:


quotes = []
for quote in soup.find_all('span',class_='text'):
    quotes.append(quote.text[1:-1])


# In[12]:


quotes


# In[ ]:





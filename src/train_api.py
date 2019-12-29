#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib.request as req
import sys
from bs4 import BeautifulSoup
    
def get_yamanote_line():
    url = "https://transit.yahoo.co.jp/traininfo/detail/21/0/"
    res = req.urlopen(url)
    soup = BeautifulSoup(res, "lxml") 
    train = soup.select_one("#main > div.mainWrp > div.labelLarge > h1").text
    status = soup.select_one("#mdServiceStatus > dl > dt").text
    if not status == "[○]平常運転":
        info = soup.select_one("#mdServiceStatus > dl > dd > p").text
        status = status + "\n  " + info

    return f'{train}: {status}'


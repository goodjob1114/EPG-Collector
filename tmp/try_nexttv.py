#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys
import urllib2
from BeautifulSoup import BeautifulSoup 

if __name__ == '__main__':

    response = urllib2.urlopen('http://www.nexttv.com.tw/program')
    html = response.read()

    soup = BeautifulSoup(html)
    tables = soup.findAll('table', attrs = {'class': 'calendar'})

    table_news = tables[0]
    table_mix = tables[1]

     

    """"
    t = etree.XML(table_news)
    rows = iter(t)
    headers = [col.text for col in next(rows)]
    for row in rows:
        values = [col.text for col in row]
        print dict(zip(headers, values))
    """"

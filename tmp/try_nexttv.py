#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys
import urllib2
import datetime
from BeautifulSoup import BeautifulSoup 

if __name__ == '__main__':

    response = urllib2.urlopen('http://www.nexttv.com.tw/program')
    html = response.read()

    soup = BeautifulSoup(html)
    tables = soup.findAll('table', attrs = {'class': 'calendar'})

    table_news = tables[0]
    table_mix = tables[1]

    th = table_news.findAll('th')

    week_date = []
    week_day = []

    for t in th:
        # t is a BeautifulSoup.Tag object
        date, day = t.string.strip().split("&nbsp;")
        week_date.append(str(datetime.date.today().year) + date.replace('/', ''))
        week_day.append(day)

    print week_date
    print week_day

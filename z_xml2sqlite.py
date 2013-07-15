#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulStoneSoup
import sqlite3

if __name__ == '__main__':

    database = sqlite3.connect("database/epg.sqlite")
    cursor = database.cursor()

    content = open('doc/epgs.com_channels.xml').read()
    soup = BeautifulStoneSoup(content)

    for channel in soup.findAll('channel'):

        c_id = channel['id']
        c_slug = channel['slug']
        c_region = channel.region.string
        c_country = channel.country.string
        c_cat = channel.category.string

        sql = """
        UPDATE epgsdotcom_channels
        SET region = '%s', country = '%s', category = '%s', slug = '%s'
        WHERE id = %d
        """ % (c_region, c_country, c_cat, c_slug, int(c_id))

        cursor.execute(sql)
        database.commit()

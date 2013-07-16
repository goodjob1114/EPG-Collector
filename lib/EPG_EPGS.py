#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging
import sqlite3
import urllib2
import xmltv

sys.path.append( os.path.abspath( os.path.dirname(__file__) ) )
from EPG_Channel import EPG_Channel

class EPG_EPGS(EPG_Channel):
    """Handling data from epgs.com"""

    def __init__(self, key = None, db = None):

        self.epgs_url = 'http://epgs.com/feeds/xml/xmltv.2.0.php?'
        self.checksum = '51e2c86bf277d'
        self.database = None

        if key is not None:
            self.checksum = key 

        if db is not None:
            self.database = sqlite3.connect(db)
            self.cursor = self.database.cursor()


    def fetch(self, utc_date = None, utc_time = None, day = None):

        region = 'us'
        sql = "SELECT id, name, slug FROM epgsdotcom_channels WHERE region = '%s'" % region
        self.cursor.execute(sql)
        channels = self.cursor.fetchall() # a list

        for channel in channels[:]: # a tuple

            xmltv_url = self.epgs_url + 'checksum=' + self.checksum + '&channel=' + str(channel[0]) # '&days=' + str(days)
            xml = urllib2.urlopen(xmltv_url) # a file-like handle
            epgs = xmltv.read_programmes(xml)

            for epg in epgs:

                name = epg['title'][0][0]
                utc_date = epg['date']
                utc_start = epg['start']
                utc_stop = epg['stop']

                if 'category' in epg.keys():
                    category = epg['category'][0][0]
                else:
                    category = ''

                sql = """
                INSERT INTO moremote_epgs (name, channel, category, utc_date, utc_start, utc_stop)
                VALUES ("%s", "%s", "%s", "%s", "%s", "%s")
                """ % (name, channel[1], category, utc_date, utc_start, utc_stop)

                print sql
                self.cursor.execute(sql)
                self.database.commit()


    def store(self, db_type = None, db_config = None):
       pass


    def info(self):
        print self.epgs_url
        print self.checksum
        print self.database
    

if __name__ == '__main__':
    test = EPG_EPGS()
    test.info()

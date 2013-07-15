#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging
import sqlite3

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

        sql = """
        SELECT id, name FROM epgsdotcom_channels
        WHERE language = ?
        """
        self.cursor.execute(sql, [("en")])

        channels = self.cursor.fetchall() # a list
        for channel in channels[:]: # a tuple
            xmltv_url = self.epgs_url + 'checksum=' + self.checksum + '&channel=' + str(channel[0]) # '&days=' + str(days)
            print u"拿 %s 從 %s" % (channel[1], xmltv_url)


    def store(self, db_type = None, db_config = None):
       pass


    def info(self):
        print self.epgs_url
        print self.checksum
        print self.database
    

if __name__ == '__main__':
    test = EPG_EPGS()
    test.info()

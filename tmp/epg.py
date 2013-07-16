#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmltv

if __name__ == '__main__':

    target = '10117_e-entertainment.xml'
    xml = open(target, 'r')
    print xml

    epgs = xmltv.read_programmes(xml)

    for epg in epgs:
        print epg['date']
        print epg['start']
        print epg['stop']
        print epg['title'][0][0]
        print epg['category'][0][0]
        print epg

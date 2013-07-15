#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from ConfigParser import SafeConfigParser

sys.path.append( os.path.abspath( os.path.join(os.path.dirname(__file__), 'lib') ) )
from EPG_EPGS import EPG_EPGS

if __name__ == '__main__':

    here = os.path.dirname(os.path.abspath(__file__))

    config_parser = SafeConfigParser()
    config_parser.read("%s/config.ini" % here)
    database = config_parser.get('sqlite', 'path')

    z = EPG_EPGS(db = database)
    z.fetch()

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ross Donaldson'
SITENAME = u'Skillet'
SITEURL = 'skillet.gastove.com'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%a, %b %d %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Paths
INPUT_PATH = 'content'
OUTPUT_PATH = 'output'

# Blogroll
LINKS =  (('Home', 'http://www.gastove.com'),
          ('Pelican', 'http://getpelican.com/'),
          ('Professional Blog', 'http://blog.gastove.com/'),)

# Social widget
SOCIAL = (('twitter', 'http://www.twitter.com/Gastove'),
          ('github', 'http://www.github.com/Gastove'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ross Donaldson'
SITENAME = u'Skillet'
SITEURL = 'skillet.gastove.com'

THEME = '../lib/theme/built-text'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%a, %b %d %Y'
DEFAULT_PAGINATION = 5
MARKUP = ('md', 'markdown')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Paths
INPUT_PATH = '../content'
OUTPUT_PATH = '../output'

# Blogroll
LINKS =  (('Home', 'http://www.gastove.com'),
          ('Pelican', 'http://getpelican.com/'),
          ('Professional Blog', 'http://blog.gastove.com/'),)

# Social widget
SOCIAL = (('twitter', 'http://www.twitter.com/Gastove'),
          ('github', 'http://www.github.com/Gastove'),)

TWITTER_USERNAME = 'gastove'

# Handy Dandy Third Parties
GOOGLE_ANALYTICS = 'UA-43979937-1'
DISQUS_SITENAME = 'skillet'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#!/usr/bin/env python
# -*- coding: utf-8 -*- #

SITENAME = 'Whyred Miui Ports'
SITEURL = 'https://whyredmiuiports.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

SLUGIFY_SOURCE = 'basename'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 20

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'https://getpelican.com/'),
#         ('Python.org', 'https://www.python.org/'),
#         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY= True
IGNORE_FILES = ['__pycache__']

USE_FOLDER_AS_CATEGORY = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (
  ('Home','/'),
  ('EU','/eu'),
  ('MMX','/mmx'),
)

PATH_METADATA = '(?P<path_no_ext>.*)\..*'
ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = '{path_no_ext}.html'
#CATEGORY_URL = '{slug}.html'
#CATEGORY_SAVE_AS = '{slug}.html'

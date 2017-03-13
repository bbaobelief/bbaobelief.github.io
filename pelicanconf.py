#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'zheng'
SITENAME = u'Opdev.cn'
METANAME = u'运维开发 | 博客'
SITEURL = 'http://192.168.16.25:8000'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh_CN'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 2

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/ops'

STATIC_PATHS = [
    'images', 
    'extra/robots.txt', 
    'extra/favicon.ico',
    'extra/images/user_logo.jpg'
]

EXTRA_PATH_METADATA = {
  'extra/favicon.ico': {'path': 'favicon.ico'},
  'extra/CNAME': {'path': 'CNAME'},
  'extra/README': {'path': 'README'},
  'extra/images/user_logo.jpg': {'path': 'user_logo.jpg'},
}

GITHUB_URL = "https://github.com/bbaobelief"

# plugin config
PLUGIN_PATHS = [u"pelican-plugins"]

PLUGINS = [
    u"sitemap", 
    u"better_codeblock_line_numbering", 
    # u"tag_cloud", 
    # u"gzip_cache", 
    # u"related_posts", 
    # u"tipue_search", 
    u"pelican-toc"
]



# sitemap plugin config
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


TOC = {
    'TOC_HEADERS' : '^h[1-6]',  # What headers should be included in the generated toc
                                # Expected format is a regular expression

    'TOC_RUN'     : 'true'      # Default value for toc generation, if it does not evaluate
                                # to 'true' no toc will be generated
}

DISPLAY_TAGS_ON_SIDEBAR = True
TAGS_URL = "tags.html"
tag_cloud = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = 'feed.xml'
FEED_MAX_ITEMS = 20



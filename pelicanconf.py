#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = u'Opdev.cn'
METANAME = u'运维开发 | 博客'
SITEURL = 'http://www.opdev.cn'
AUTHOR = u'zheng'
AUTHOR_QQ = u'773889242'
AUTHOR_EMAIL = u'bbaobelief@163.com'
ABOUT_ME_SUMMARY = u'90后，男，耳机发烧友，古典、新世纪、美剧迷。现就职于百度某公司，任运维开发工程师。'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL

YEAR_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/{date:%m}/index.html'

# Blogroll
LINKS = (('运维开发', 'http://www.opdev.cn/'),
         ('fashao.me', 'http://www.fashao.me/'),
         ('ShouJiong', 'http://shoujiong.org'),
         ('姚大师', 'http://pengyao.org/'),
         ('普拉多VX', 'http://www.roddypy.com/'),
         ('阿布的博客', 'http://www.abuve.com/'),
        )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 20


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/ops'

DEFAULT_USER_LOGO = u'default.png'

STATIC_PATHS = [
    'images', 
    'extra/robots.txt', 
    'extra/favicon.ico',
    'extra/images/dashang_weixin.png',
    'extra/images/dashang_zhifubao.png',
    'extra/images/%s' % DEFAULT_USER_LOGO
]

EXTRA_PATH_METADATA = {
  'extra/favicon.ico': {'path': 'favicon.ico'},
  'extra/CNAME': {'path': 'CNAME'},
  'extra/README': {'path': 'README'},
  'extra/images/%s' % DEFAULT_USER_LOGO: {'path': DEFAULT_USER_LOGO},
}


TEMPLATE_PAGES = {
    "404.html": "404.html",
}


GITHUB_URL = "https://github.com/bbaobelief"
CHANGYAN_APPID = "cysUqW1oc"
CHANGYAN_APPKEY = "fa1ee41f1942bf4ed22fcbee5890fb17"

BAIDU_ANALYTICS = "a14887a9f31eeff5459d8cbbf3da3c4f" 

# plugin config
PLUGIN_PATHS = [u"pelican-plugins"]

PLUGINS = [
    u"sitemap", 
    u"better_codeblock_line_numbering", 
    u"tag_cloud", 
    # u"gzip_cache", 
    # u"related_posts", 
    u"tipue_search", 
    u"pelican-toc"
]


# Tipue Search
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search',))
SEARCH_URL = '/search'


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

    'TOC_RUN'     : 'false'     # Default value for toc generation, if it does not evaluate
                                # to 'true' no toc will be generated
}

# PYGMENTS_RST_OPTIONS = {'classprefix': 'highlight', 'linenos': 'code-line'}

# MARKDOWN = {
    # 'extension_configs': {
        # 'markdown.extensions.codehilite': {'css_class': 'highlight'},
        # 'markdown.extensions.extra': {},
        # 'markdown.extensions.meta': {},
    # },
    # 'output_format': 'html5',
# }

DISPLAY_TAGS_ON_SIDEBAR = True
TAGS_URL = "tags.html"
tag_cloud = True

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = None
FEED_ALL_RSS = 'feed.xml'
FEED_MAX_ITEMS = 20


# baidu analytics
# BAIDU_ANALYTICS 



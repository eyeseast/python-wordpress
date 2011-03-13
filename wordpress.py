"""
A Python client for the WordPress JSON API
"""
# This library is aimed at easier communication between
# Python-based projects and a wordpress installation.

import httplib2
import urllib
try:
    import json
except ImportError:
    import simplejson as json

# Setting debug to True will add requested URLs to returned JSON
DEBUG = False

# ## WordPress
# Create an instance with a blog's URL, path prefix (`api` by default)
# and cache setting. WordPress uses httplib2 under the hood, and caching
# is pluggable. It's possible to pass in a `django.core.cache.cache` object
# here to use the same cache backend you've set up for a Django project.
class WordPress(object):
    """
    The main wrapper
    """
    def __init__(self, blog_url, prefix='api', cache='.cache'):
        self.blog_url = blog_url
        self.prefix = prefix
        self.base_url = urlparse.urljoin(blog_url, prefix)
        self._http = httplib2.Http(cache)

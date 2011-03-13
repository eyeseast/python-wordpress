#!/usr/bin/env python

import httplib2
import os
import unittest
import urlparse
from wordpress import WordPress, json, DEFAULT_METHODS

http = httplib2.Http()

class WordPressTest(unittest.TestCase):
    
    def setUp(self):
        self.blog_url = "http://localhost:8888/wordpress"
        self.wp = WordPress(self.blog_url, cache=None)
    
    def check_response(self, result, url):
        "Check that the parsed result matches the given URL"
        r, c = http.request(url)
        c = json.loads(c)
        self.assertEqual(c, result)
        
    def test_get_info(self):
        "Test basic info"
        result = self.wp.info()
        self.check_response(result, 'http://localhost:8888/wordpress/?dev=1&json=info')
    
    def test_get_recent_posts(self):
        "Test getting recent posts"
        result = self.wp.get_recent_posts()
        self.check_response(result, 'http://localhost:8888/wordpress/api/get_recent_posts/?dev=1')
    
    def test_get_post(self):
        """Test getting a single post"""
        result = self.wp.get_post(id=1)
        self.check_response(result, 'http://localhost:8888/wordpress/?json=get_post&id=1&dev=1')
        
    def test_get_categories(self):
        """Test getting all active categories"""
        result = self.wp.get_category_index()
        self.check_response(result, 'http://localhost:8888/wordpress/?json=get_category_index&dev=1')
    
    def test_bad_method(self):
        """Trying to call something that isn't a real method should raise AttributeError"""
        # for the record, this is an odd way to test this
        try:
            self.wp.do_something_bad
            self.fail()
        except AttributeError:
            pass
    

if __name__ == '__main__':
    unittest.main()
#!/usr/bin/env python

import httplib2
import os
import unittest
import urlparse
from wordpress import WordPress, json, DEFAULT_METHODS

class WordPressTest(unittest.TestCase):
    
    def setUp(self):
        self.blog_url = os.environ.get('WORDPRESS_BLOG_URL', 'http://localhost:8888/wordpress')
        self.http = httplib2.Http()
        self.wp = WordPress(self.blog_url, cache=None)
    
    def check_response(self, result, url):
        "Check that the parsed result matches the given URL"
        r, c = self.http.request(url)
        c = json.loads(c)
        self.assertEqual(c, result)
        
    def test_get_info(self):
        "Test basic info"
        result = self.wp.info()
        self.check_response(result, '%s/?dev=1&json=info' % self.blog_url)
    
    def test_get_recent_posts(self):
        "Test getting recent posts"
        result = self.wp.get_recent_posts()
        self.check_response(result, '%s/api/get_recent_posts/?dev=1' % self.blog_url)
    
    def test_get_post(self):
        """Test getting a single post"""
        # don't assume there's a post with ID 1
        # this assumes get_recent_posts works, will raise KeyError if not
        results = self.wp.get_recent_posts(count=3)
        for post in results['posts']:
            ID = post['id']
            post = self.wp.get_post(id=ID)
            self.check_response(post, '%s/?json=get_post&id=%s&dev=1' % (self.blog_url, ID))
        
    def test_get_categories(self):
        """Test getting all active categories"""
        result = self.wp.get_category_index()
        self.check_response(result, '%s/?json=get_category_index&dev=1' % self.blog_url)
    
    def test_bad_method(self):
        """Trying to call something that isn't a real method should raise AttributeError"""
        # for the record, this is an odd way to test this
        with self.assertRaises(AttributeError):
            self.wp.do_something_bad
    

if __name__ == '__main__':
    unittest.main()
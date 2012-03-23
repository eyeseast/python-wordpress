Python WordPress
==================

A simple Python library for talking to Wordpress in JSON. This library relies on the [WordPress JSON API plugin][1]. This won't work if your WordPress site doesn't have the plugin installed.

  [1]: http://wordpress.org/extend/plugins/json-api/ "WordPress JSON API"

Install:

    $ pip install python-wordpress

Or `git clone` and `python setup.py install` and such.

Usage:

    >>> from wordpress import WordPress
    >>> wp = WordPress('http://example.com/blog/')
    >>> posts = wp.get_recent_posts()

For now, this only covers the *read* portions of the API under the `core` controller. See the [WordPress JSON API documentation][2] for details.

  [2]: http://wordpress.org/extend/plugins/json-api/other_notes/

Tests assume a WordPress blog running on [MAMP][3] at http://localhost:8888/wordpress, but you can change that by setting `WORDPRESS_BLOG_URL` as an environment variable, like so:

    WORDPRESS_BLOG_URL=http://wordpress.local.host python test.py

  [3]: http://www.mamp.info/en/index.html "MAMP!"
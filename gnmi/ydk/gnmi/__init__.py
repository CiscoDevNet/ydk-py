"""
    gnmi/__init__.py

    The code below is taken from Flask <http://flask.pocoo.org> project, and
    the original docstring is listed below.

    Redirect imports for extensions.  This module basically makes it possible
    for us to transition from flaskext.foo to flask_foo without having to
    force all extensions to upgrade at the same time.
    When a user does ``from flask.ext.foo import bar`` it will attempt to
    import ``from flask_foo import bar`` first and when that fails it will
    try to import ``from flaskext.foo import bar``.
    We're switching from namespace packages because it was just too painful for
    everybody involved.
    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""


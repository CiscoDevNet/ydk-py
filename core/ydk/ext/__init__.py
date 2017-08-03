"""
    ydk.ext

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
import atexit
import importlib


def setup():
    from ..exthook import ExtensionImporter
    importer = ExtensionImporter(['ydk_.%s'], __name__)
    importer.install()

def register_exit():

    def exit_handler():
        # allow sys.exit with logging for main block
        main = importlib.import_module('__main__')
        main.__dict__.clear()

    atexit.register(exit_handler)

register_exit()
setup()

del setup

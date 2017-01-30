"""
Things to Remember
Programs often need to run in multiple deployment environments that each have unique assumptions and configurations.
You can tailor a module's contents to different deployment environments by using normal Python statements in module scope.
Module contents can be the product of any external condition, including host introspection through the sys and os modules.
"""

# dev_main.py
TESTING = True
import db_connection
db = db_connection.Database()

# prod_main.py
TESTING = False
import db_connection
db = db_connection.Database()

# db_connection.py
import __main__
class TestingDatabase(object):
    # ...
    pass
class RealDatabase(object):
    # ...
    pass
if __main__.TESTING:
    Database = TestingDatabase
else:
    Database = RealDatabase

# db_connection.py
import sys
class Win32Database(object):
    # ...
    pass
class PosixDatabase(object):
    # ...
    pass
if sys.platform.startswith('win32'):
    Database = Win32Database
else:
    Database = PosixDatabase
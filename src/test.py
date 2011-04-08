'''
Created on Apr 8, 2011

@author: cgueret
'''

import os
import dbus
from sugar.datastore import datastore

if os.path.exists("/tmp/olpc-session-bus"):
    os.environ["DBUS_SESSION_BUS_ADDRESS"] = "unix:path=/tmp/olpc-session-bus"

if __name__ == "__main__":
    try:
        query = {}
        query['query'] = '*Terminal*'
        objects, count = datastore.find(query, limit=2, sorting='-mtime')
        print objects, count
    except dbus.DBusException:
        print 'ERROR: Unable to connect to the datastore.\n'
    except Exception, e:
        print 'ERROR: %s' % (e)
        

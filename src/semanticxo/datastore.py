'''
Created on Jan 24, 2011

@author: cgueret
'''
import logging
import dbus.service
import uuid
import time
import os

# the name used by the logger
DS_LOG_CHANNEL = 'org.laptop.sugar.DataStore'

# the bus the datastore uses
DS_SERVICE = "org.laptop.sugar.DataStore"
DS_DBUS_INTERFACE = "org.laptop.sugar.DataStore"
DS_OBJECT_PATH = "/org/laptop/sugar/DataStore"

# logger
logger = logging.getLogger(DS_LOG_CHANNEL)

class DataStore(dbus.service.Object):
    '''
    D-Bus API and logic for connecting all the other components.
    '''
    def __init__(self, **options):
        '''
        Constructor
        '''
        bus_name = dbus.service.BusName(DS_SERVICE, bus=dbus.SessionBus(), replace_existing=False, allow_replacement=False)
        dbus.service.Object.__init__(self, bus_name, DS_OBJECT_PATH)
        print 'fdfd'
    @dbus.service.method(DS_DBUS_INTERFACE, in_signature='a{sv}sb', out_signature='s', async_callbacks=('async_cb', 'async_err_cb'), byte_arrays=True)
    def create(self, props, file_path, transfer_ownership, async_cb, async_err_cb):
        print 'create'
        '''
        Create a new object in the datastore
        '''
        
        # Get a uuid
        uid = str(uuid.uuid4())
        logging.debug('datastore.create %r', uid)
        
        # Insert missing properties if needed
        if 'timestamp' not in props:
            props['timestamp'] = int(time.time())
        if 'creation_time' not in props:
            props['creation_time'] = props['timestamp']
        if os.path.exists(file_path):
            props['filesize'] = os.stat(file_path).st_size
        else:
            props['filesize'] = 0
            
        # Create the object and assign predicate values
        
        # Execute a SPARQL query to insert the data
    
        # Signal
        self.Created(uid)
        
    @dbus.service.signal(DS_DBUS_INTERFACE, signature="s")
    def Created(self, uid):
        pass

    @dbus.service.method(DS_DBUS_INTERFACE, in_signature='sa{sv}sb', out_signature='', async_callbacks=('async_cb', 'async_err_cb'), byte_arrays=True)
    def update(self, uid, props, file_path, transfer_ownership, async_cb, async_err_cb):
        print 'update'
        # Signal
        self.Updated(uid)
    
    @dbus.service.signal(DS_DBUS_INTERFACE, signature="s")
    def Updated(self, uid):
        pass

    @dbus.service.method(DS_DBUS_INTERFACE, in_signature='a{sv}as', out_signature='aa{sv}u')
    def find(self, query, properties):
        '''
        Search for an object
        '''
        print 'find'
        return [], 0

    @dbus.service.method(DS_DBUS_INTERFACE, in_signature='s', out_signature='s', sender_keyword='sender')
    def get_filename(self, uid, sender=None):
        pass

    @dbus.service.method(DS_DBUS_INTERFACE, in_signature='s', out_signature='a{sv}')
    def get_properties(self, uid):
        pass
    
    @dbus.service.method(DS_DBUS_INTERFACE, in_signature='sa{sv}', out_signature='as')
    def get_uniquevaluesfor(self, propertyname, query=None):
        pass
    
    @dbus.service.method(DS_DBUS_INTERFACE, in_signature='s', out_signature='')
    def delete(self, uid):
        self.Deleted(uid)

    @dbus.service.signal(DS_DBUS_INTERFACE, signature="s")
    def Deleted(self, uid):
        pass

    @dbus.service.signal(DS_DBUS_INTERFACE)
    def Stopped(self):
        pass

    @dbus.service.method(DS_DBUS_INTERFACE, in_signature="sa{sv}", out_signature='s')
    def mount(self, uri, options=None):
        return ''

    @dbus.service.method(DS_DBUS_INTERFACE, in_signature="", out_signature="aa{sv}")
    def mounts(self):
        return [{'id': 1}]

    @dbus.service.signal(DS_DBUS_INTERFACE, signature="a{sv}")
    def Mounted(self, descriptior):
        pass
    
    @dbus.service.method(DS_DBUS_INTERFACE, in_signature="s", out_signature="")
    def unmount(self, mountpoint_id):
        pass

    @dbus.service.signal(DS_DBUS_INTERFACE, signature="a{sv}")
    def Unmounted(self, descriptor):
        pass
        

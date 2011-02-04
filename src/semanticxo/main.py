'''
Created on Jan 24, 2011

@author: cgueret
'''
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
DBusGMainLoop(set_as_default=True)
import gobject

DS_SERVICE = "org.laptop.sugar.DataStore"
DS_DBUS_INTERFACE = "org.laptop.sugar.DataStore"
DS_OBJECT_PATH = "/org/laptop/sugar/DataStore"

def main():
    bus_name = dbus.service.BusName(DS_SERVICE,
                                    bus=dbus.SessionBus(),
                                    replace_existing=False,
                                    allow_replacement=False)
    #dbus.service.Object.__init__(self,bus_name, DS_OBJECT_PATH)
    dbus.service.Object(None, DS_OBJECT_PATH, bus_name)
    print "hello"
    loop = gobject.MainLoop()
    loop.run()

if __name__ == '__main__':
    main()

#!/usr/bin/env python2
import sys
import os
import signal
import logging
import gobject
import dbus.service
import dbus.mainloop.glib
import dbus.glib
from semanticxo.datastore import DataStore
from sugar import logger

# Path handling
profile = os.environ.get('SUGAR_PROFILE', 'default')
base_dir = os.path.join(os.path.expanduser('~'), '.sugar', profile)
log_dir = os.path.join(base_dir, "logs")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# build the datastore
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SessionBus()
connected = True

ds = DataStore()

# and run it
mainloop = gobject.MainLoop()


def handle_disconnect():
    mainloop.quit()
    logging.debug("Datastore disconnected from the bus.")


def handle_shutdown(signum, frame):
    mainloop.quit()
    raise SystemExit("Shutting down on signal %s" % signum)

bus.set_exit_on_disconnect(False)
bus.add_signal_receiver(handle_disconnect,
                        signal_name='Disconnected',
                        dbus_interface='org.freedesktop.DBus.Local')

signal.signal(signal.SIGHUP, handle_shutdown)
signal.signal(signal.SIGTERM, handle_shutdown)


def main():
    try:
        mainloop.run()
    except KeyboardInterrupt:
        logging.info("DataStore shutdown by user")
    except:
        logging.error("Datastore shutdown with error", exc_info=sys.exc_info())

main()

ds.stop()

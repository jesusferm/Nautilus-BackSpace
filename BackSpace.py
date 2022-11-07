#!/usr/bin/env python
# created by linuxitos
import gi

gi.require_version('Nautilus', '4.0')
gi.require_version('Gtk', '4.0')
from gi.repository import GObject, Nautilus, Gtk, GLib


def idle_callback(*args):
    app = Gtk.Application.get_default()
    app.set_accels_for_action("win.up", ["BackSpace"])
    return False


def window_added(*args):
    GLib.idle_add(idle_callback, None)


class BackspaceBack(GObject.GObject, Nautilus.ColumnProvider):
        app = Gtk.Application.get_default()
        app.set_accels_for_action("win.up", ["BackSpace"])
        app.connect("window-added", window_added)

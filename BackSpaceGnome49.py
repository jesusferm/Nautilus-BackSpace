#!/usr/bin/env python
# created by linuxitos (mod GNOME 49)

import gi
import os

gi.require_version('Nautilus', '4.1')
gi.require_version('Gtk', '4.0')
gi.require_version('Gdk', '4.0')

from gi.repository import GObject, Nautilus, Gtk, Gdk

class BackspaceBack(GObject.GObject, Nautilus.InfoProvider):

    def __init__(self):
        super().__init__()

        app = Gtk.Application.get_default()
        if not app:
            print("[BackspaceBack] Gtk.Application.get_default() is None", file=os.sys.stderr)
            return

        app.connect("window-added", self.on_window_added)

        for window in app.get_windows():
            if isinstance(window, Gtk.ApplicationWindow):
                self._attach_controller(window)

    def update_file_info(self, file: Nautilus.FileInfo):
        return

    def on_window_added(self, app, window):
        if isinstance(window, Gtk.ApplicationWindow):
            self._attach_controller(window)

    def _attach_controller(self, window: Gtk.Window):
        if getattr(window, "_backspace_nav_attached", False):
            return

        key_controller = Gtk.EventControllerKey.new()
        key_controller.connect("key-pressed", self.on_key_pressed, window)
        window.add_controller(key_controller)

        window._backspace_nav_attached = True

    def on_key_pressed(self, controller, keyval, keycode, state, window: Gtk.Window):
        if keyval != Gdk.KEY_BackSpace:
            return False

        if state & Gtk.accelerator_get_default_mod_mask():
            return False

        focus_widget = window.get_focus()

        if isinstance(focus_widget, Gtk.Editable):
            return False

        try:
            window.activate_action("slot.up", None)
            return True
        except Exception as e:
            print(f"[BackspaceBack] Error al activar 'slot.up': {e}", file=os.sys.stderr)
            return False

def init():
    return BackspaceBack()

# LiveControl3.py
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.ButtonElement import ButtonElement
from _Framework.DeviceComponent import DeviceComponent
from _Framework.TransportComponent import TransportComponent

import importlib

class LoggingError(Exception):
    pass


class LiveControl3(ControlSurface):

    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        self.show_message("LiveControl 3 ready")
        
        path = importlib.machinery.PathFinder().find_module("Live").get_filename()

        with self.component_guard():
            self._setup_device_and_transport_control()
        raise LoggingError("Log:" + (path))

    def _setup_device_and_transport_control(self):
        self._device = DeviceComponent()
        self.transport = TransportComponent()
        self.transport.set_play_button(ButtonElement(1, 1, 0, 104)) # ButtonElement(is_momentary, msg_type, channel, identifier)
        self.transport.set_stop_button(ButtonElement(1, 1, 0, 105))
        self.transport.set_record_button(ButtonElement(1, 1, 0, 106))



        

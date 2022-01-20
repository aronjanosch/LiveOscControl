# LiveControl3.py
import os
import logging

import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.ButtonElement import ButtonElement
from _Framework.DeviceComponent import DeviceComponent
from _Framework.TransportComponent import TransportComponent


logger = logging.getLogger("LiveOSCControl")
tmp_dir = "/tmp"
log_path = os.path.join(tmp_dir, "LiveOSCC.log")
file_handler = logging.FileHandler(log_path)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('(%(asctime)s) [%(levelname)s] %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class LoggingError(Exception):
    pass


class LiveControl3(ControlSurface):

    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        self.show_message("LiveControl 3 ready")
        logger.info("Script loaded")
        logger.info(Live.Application.get_application())

        with self.component_guard():
            self._setup_device_and_transport_control()
            self._live_test()

    def _setup_device_and_transport_control(self):
        self._device = DeviceComponent()
        self.transport = TransportComponent()
        self.transport.set_play_button(ButtonElement(1, 1, 0, 104)) # ButtonElement(is_momentary, msg_type, channel, identifier)
        self.transport.set_stop_button(ButtonElement(1, 1, 0, 105))
        self.transport.set_record_button(ButtonElement(1, 1, 0, 106))

    def _live_test(self):
        self.button_up = ButtonElement(1, 1, 0, 104)

        if self.button_up.is_pressed():
            logger.info(str(Live.Song.Song.is_playing()))



        

# LiveControl3.py

from . import handlers

import os
import logging

import Live
from _Framework.ControlSurface import ControlSurface


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
        self.handlers =[]
        self.show_message("LiveControl 3 ready")
        logger.info("Script loaded")

        self.init_liveosc()

    def init_liveosc(self):
        logger.info("Instantiate Handlers")
        with self.component_guard():
            self.handlers = [
                handlers.SongHandler(song=self.song())
            ]



        

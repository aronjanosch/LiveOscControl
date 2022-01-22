# LiveControl3.py

from . import handlers
import config

import os
import logging

import Live
from _Framework.ControlSurface import ControlSurface

if config.DEBUG:
    logging_level = logging.DEBUG
else:
    logging_level = logging.CRITICAL
logger = logging.getLogger("LiveOSCControl")
logging.basicConfig(level=logging_level,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=config.LOG_FILE,
                    filemode='w')


class LiveControl3(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        self.handlers = []
        self.show_message("LiveControl 3 ready")
        logger.info("Script loaded")

        self.init_liveosc()

    def init_liveosc(self):
        logger.info("Instantiate Handlers")
        with self.component_guard():
            self.handlers = [
                handlers.SongHandler(song=self.song())
            ]

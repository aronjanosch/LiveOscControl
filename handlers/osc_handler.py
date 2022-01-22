import errno
import logging
import socket
import traceback
from typing import Callable, Tuple, Any
from ..pythonosc.osc_message_builder import OscMessageBuilder
from ..pythonosc.osc_message import OscMessage, ParseError

import config


class OSCServer:
    def __init__(self, listening_address=('127.0.0.1', config.OSC_LISTEN_PORT),
                 response_address=('127.0.0.1', config.OSC_RESPONSE_PORT)):

        self.logger = logging.getLogger("LiveOSCControl")

        self.listening_address = listening_address
        self.response_address = response_address

        self.logger.info("Starting OSC server (listening %s, response %s" %
                         (str(self.listening_address), str(self.response_address)))

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setblocking(0)
        self.socket.bind(self.listening_address)
        self.callbacks = {}

    def add_handler(self, address: str, handler: Callable):
        self.callbacks[address] = handler

    def clear_handler(self):
        self.callbacks = {}

    def send(self, address: str, params: Tuple[Any] = ()):
        # TO be implemented
        pass

    def receive(self):
        try:
            while True:
                data, addr = self.socket.recfrom(65536)
                try:
                    message = OscMessage(data)

                    if message.address in self.callbacks:
                        callback = self.callbacks[message.address]
                        rv = callback(message.params)
                        if rv is not None:
                            self.send(message.address, rv)
                        else:
                            self.logger.error("Unknown OSC address: " + message.address)
                except ParseError:
                    self.logger.error("OSC parse error: " + traceback.format_exc())

        except socket.error as e:
            if e.errno == errno.EAGAIN:
                return
            else:
                self.logger.error("Socket error: " + traceback.format_exc())
        except Exception as e:
            self.logger.error("Error handling message: " + traceback.format_exc())


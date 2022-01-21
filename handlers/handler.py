from ableton.v2.control_surface.component import Component
import logging


class OSCHandler:
    def __init__(self):
        self.logger = logging.getLogger("LiveOSCControl")

    #--------------------------------------------------------------------------------
    # Generic callbacks
    #--------------------------------------------------------------------------------

    def _add_listener(self, target, prop):
        """
        creates listener at target (Live)
        :param target: Live target
        :param listener:
        :return:
        """
        def callback():
            value = getattr(target, prop)
            self.logger.info("Property %s has changed to: %s" % (prop, value))
        listener_func = getattr(target, "add_" + prop + "_listener")
        listener_func(callback)
        self.logger.info("Added Listener for" + str(prop))
        return callback

#LiveControl3.py
#This is a stripped-down script, which uses the Framework classes to assign MIDI notes to play, stop and record.
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.InputControlElement import *
from _Framework.SliderElement import SliderElement
from _Framework.ButtonElement import ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.ChannelStripComponent import ChannelStripComponent
from _Framework.DeviceComponent import DeviceComponent
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.SessionZoomingComponent import SessionZoomingComponent
from _Framework.TransportComponent import TransportComponent


class LoggingError(Exception):
    pass

class LiveControl3(ControlSurface):

    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        self.show_message("LiveControl 3 ready")
        raise LoggingError("Log:" + str(Live.__file__))

        with self.component_guard():
            self._setup_device_and_transport_control()

        

    def _setup_device_and_transport_control(self):
        self._device = DeviceComponent()
        self.transport = TransportComponent() #Instantiate a Transport Component
        self.transport.set_play_button(ButtonElement(1, 1, 0, 104)) #ButtonElement(is_momentary, msg_type, channel, identifier)
        self.transport.set_stop_button(ButtonElement(1, 1, 0, 105))
        self.transport.set_record_button(ButtonElement(1, 1, 0, 106))



        

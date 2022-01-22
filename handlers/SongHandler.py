from .handler import Handler


class SongHandler(Handler):
    def __init__(self, song, manager):
        self.song = song
        super().__init__(manager)
        self.song_listeners = ['tempo', 'signature_numerator', 'signature_denominator', 'is_playing', 'record_mode',
                               'metronome', 'loop', 'overdub', 'clip_trigger_quantization',
                               'midi_recording_quantization', 'back_to_arranger', 'current_song_time']
        self.song_view_listeners = ['detail_clip', 'selected_scene', 'selected_track']

        self.properties = {'is_playing': {'type': 'attribute', 'readonly': True},
                           'metronome': {'type': 'attribute'},
                           'tempo': {'type': 'attribute'},
                           'signature_numerator': {'type': 'attribute'},
                           'signature_denominator': {'type': 'attribute'},
                           'record_mode': {'type': 'attribute'},
                           'nudge_up': {'type': 'attribute'},
                           'nudge_down': {'type': 'attribute'},
                           'loop': {'type': 'attribute'},
                           'undo': {'type': 'function'},
                           'redo': {'type': 'function'},
                           'jump_to_next_cue': {'type': 'function'},
                           'jump_to_prev_cue': {'type': 'function'},
                           'set_or_delete_cue': {'type': 'function'},
                           'stop_all_clips': {'type': 'function'},
                           'scrub_by': {'type': 'function', 'parameters': 1},
                           'create_scene': {'type': 'function', 'parameters': 1, 'parameter_type': "int"},
                           'create_midi_track': {'type': 'function', 'parameters': 1, 'parameter_type': "int"},
                           'create_audio_track': {'type': 'function', 'parameters': 1, 'parameter_type': "int"},
                           'create_return_track': {'type': 'function'},
                           'delete_scene': {'type': 'function', 'parameters': 1, 'parameter_type': "int"},
                           'delete_track': {'type': 'function', 'parameters': 1, 'parameter_type': "int"},
                           'duplicate_scene': {'type': 'function', 'parameters': 1, 'parameter_type': "int"},
                           'duplicate_track': {'type': 'function', 'parameters': 1, 'parameter_type': "int"}}

        self.callbacks = {}
        self.add_listeners()

    def add_listeners(self):
        self.logger.info("Adding Song Listeners")
        for listener in self.song_listeners:
            self.callbacks[listener] = self._add_listener(self.song, listener)

    def add_osc_callbacks(self):
        for key, value in self.callbacks.items():
            self.osc_handler.add_handler("/song/get")


# Listneres werden gesendet von OSC Serve. Da handler hier Server importiert können acuh heir callbacks verwaltet werden
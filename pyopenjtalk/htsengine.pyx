# coding: utf-8
# cython: boundscheck=True, wraparound=True
# cython: c_string_type=unicode, c_string_encoding=ascii

import numpy as np

cimport numpy as np
np.import_array()

cimport cython
from libc.stdlib cimport malloc, free

from htsengine cimport HTS_Engine
from htsengine cimport (
    HTS_Engine_initialize, HTS_Engine_load, HTS_Engine_clear, HTS_Engine_refresh,
    HTS_Engine_get_sampling_frequency, HTS_Engine_get_fperiod,
    HTS_Engine_set_speed, HTS_Engine_add_half_tone,
    HTS_Engine_synthesize_from_strings,
    HTS_Engine_get_generated_speech, HTS_Engine_get_nsamples,
    HTS_Engine_set_gv_weight, HTS_Engine_get_state_duration,
    HTS_Engine_get_nstate
)

cdef class HTSEngine(object):
    """HTSEngine

    Args:
        voice (bytes): File path of htsvoice.
    """
    cdef HTS_Engine* engine
    cdef size_t label_len

    def __cinit__(self, bytes voice=b"htsvoice/mei_normal.htsvoice"):
        self.engine = new HTS_Engine()

        HTS_Engine_initialize(self.engine)

        if self.load(voice) != 1:
          self.clear()
          raise RuntimeError("Failed to initalize HTS_Engine")

    def load(self, bytes voice):
        cdef char* voices = voice
        cdef char ret
        ret = HTS_Engine_load(self.engine, &voices, 1)
        return ret

    def get_sampling_frequency(self):
        """Get sampling frequency
        """
        return HTS_Engine_get_sampling_frequency(self.engine)

    def get_fperiod(self):
        """Get frame period"""
        return HTS_Engine_get_fperiod(self.engine)

    def set_speed(self, speed=1.0):
        """Set speed

        Args:
            speed (float): speed
        """
        HTS_Engine_set_speed(self.engine, speed)

    def add_half_tone(self, half_tone=0.0):
        """Additional half tone in log-f0

        Args:
            half_tone (float): additional half tone
        """
        HTS_Engine_add_half_tone(self.engine, half_tone)
    
    def set_gv_weight_log_f0(self, float f):
        HTS_Engine_set_gv_weight(self.engine, 1, f)

    def get_phoneme_length(self):
        cdef size_t label_len = self.label_len
        cdef size_t fperiod = HTS_Engine_get_fperiod(self.engine)
        cdef size_t nstate = HTS_Engine_get_nstate(self.engine)
        cdef size_t state = 0
        cdef size_t duration
        cdef np.ndarray frame = np.zeros([label_len], dtype=np.uint64)
        for i in range(label_len):
            duration = 0
            for j in range(nstate):
                duration += HTS_Engine_get_state_duration(self.engine, state)
                state += 1
            frame[i] = duration * fperiod
        return frame

    def synthesize(self, list labels):
        """Synthesize waveform from list of full-context labels

        Args:
            labels: full context labels

        Returns:
            np.ndarray: speech waveform
        """
        self.synthesize_from_strings(labels)
        x = self.get_generated_speech()
        self.refresh()
        return x

    def synthesize_from_strings(self, list labels):
        """Synthesize from strings"""
        cdef size_t num_lines = len(labels)
        self.label_len = num_lines
        cdef char **lines = <char**> malloc((num_lines + 1) * sizeof(char*))
        for n in range(len(labels)):
            lines[n] = <char*>labels[n]

        cdef char ret = HTS_Engine_synthesize_from_strings(self.engine, lines, num_lines)
        free(lines)
        if ret != 1:
            raise RuntimeError("Failed to run synthesize_from_strings")

    def get_generated_speech(self):
        """Get generated speech"""
        cdef size_t nsamples = HTS_Engine_get_nsamples(self.engine)
        cdef np.ndarray speech = np.zeros([nsamples], dtype=np.float64)
        cdef size_t index
        for index in range(nsamples):
            speech[index] = HTS_Engine_get_generated_speech(self.engine, index)
        return speech

    def get_fullcontext_label_format(self):
        """Get full-context label format"""
        return (<bytes>HTS_Engine_get_fullcontext_label_format(self.engine)).decode("utf-8")

    def refresh(self):
        self.label_len = 0
        HTS_Engine_refresh(self.engine)

    def clear(self):
        self.label_len = 0
        HTS_Engine_clear(self.engine)

    def __dealloc__(self):
        self.clear()
        del self.engine

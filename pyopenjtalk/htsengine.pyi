import ctypes
from typing import List

import numpy

class HTSEngine:
    def __init__(self, voice: bytes = b"htsvoice/mei_normal.htsvoice") -> None:
        """HTSEngine
        Args:
            voice (bytes): File path of htsvoice.
        """
        raise RuntimeError("Failed to initalize HTS_Engine")
    def load(self, voice: bytes) -> bytes: ...
    def get_sampling_frequency(self) -> int:
        """Get sampling frequency"""
        pass
    def get_fperiod(self) -> int:
        """Get frame period"""
        pass
    def set_speed(self, speed: float = 1.0) -> None:
        """Set speed
        Args:
            speed (float): speed
        """
        pass
    def add_half_tone(self, half_tone: float = 0.0) -> None:
        """Additional half tone in log-f0
        Args:
            half_tone (float): additional half tone
        """
        pass
    def synthesize(self, labels: List[str]) -> numpy.ndarray:
        """Synthesize waveform from list of full-context labels
        Args:
            labels: full context labels
        Returns:
            np.ndarray: speech waveform
        """
        pass
    def synthesize_from_strings(self, labels: List[str]) -> None:
        """Synthesize from strings"""
        raise RuntimeError("Failed to run synthesize_from_strings")
    def get_generated_speech(self) -> numpy.ndarray:
        """Get generated speech"""
        pass
    def get_fullcontext_label_format(self) -> str:
        """Get full-context label format"""
        pass
    def refresh(self) -> None: ...
    def clear(self) -> None: ...
    def __dealloc__(self) -> None: ...

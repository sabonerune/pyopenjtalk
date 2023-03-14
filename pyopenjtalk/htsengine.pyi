from typing import List

import numpy

class HTSEngine:
    def __init__(self, voice: bytes = b"htsvoice/mei_normal.htsvoice") -> None:
        """HTSEngine
        Args:
            voice (bytes): File path of htsvoice.
        """
        pass
    def load(self, voice: bytes) -> bytes:
        pass
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
    def set_gv_weight_log_f0(self, f: float) -> None:
        pass
    def get_phoneme_length(self) -> numpy.ndarray:
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
        pass
    def get_generated_speech(self) -> numpy.ndarray:
        """Get generated speech"""
        pass
    def get_fullcontext_label_format(self) -> str:
        """Get full-context label format"""
        pass
    def refresh(self) -> None:
        pass
    def clear(self) -> None:
        pass
    def __dealloc__(self) -> None:
        pass

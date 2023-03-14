from typing import List, Union

class OpenJTalk:
    def __init__(
        self, dn_mecab: bytes = b"/usr/local/dic", user_mecab: bytes = b""
    ) -> None:
        """OpenJTalk
        Args:
            dn_mecab (bytes): Dictionaly path for MeCab.
            user_mecab (bytes): Dictionary path for MeCab userdic.
                This option is ignored when empty bytestring is given.
                Default is empty.
        """
        raise RuntimeError("Failed to initalize Mecab")
    def _clear(self) -> None:
        pass
    def _load(self, dn_mecab: bytes, user_mecab: bytes) -> int:
        pass
    def run_frontend(self, text: str) -> List[dict]:
        """Run OpenJTalk's text processing frontend"""
        pass
    def make_label(self, features) -> List[str]:
        """Make full-context label"""
        pass
    def g2p(
        self, text: str, kana: bool = False, join: bool = True
    ) -> Union[List[str], str]:
        """Grapheme-to-phoeneme (G2P) conversion"""
        pass
    def __dealloc__(self) -> None:
        pass

def CreateUserDict(dn_mecab: bytes, path: bytes, out_path: bytes) -> None:
    pass

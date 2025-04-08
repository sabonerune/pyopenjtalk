# flake8: noqa
from collections.abc import Iterable, Mapping
from typing import Literal, TypedDict, overload

class _NJDFeature(TypedDict):
    string: str
    pos: str
    pos_group1: str
    pos_group2: str
    pos_group3: str
    ctype: str
    cform: str
    orig: str
    read: str
    pron: str
    acc: int
    mora_size: int
    chain_rule: str
    chain_flag: int

class OpenJTalk:
    def __init__(
        self, dn_mecab: bytes = b"/usr/local/dic", userdic: bytes = b""
    ) -> None:
        """OpenJTalk

        Args:
            dn_mecab (bytes): Dictionaly path for MeCab.
            userdic (bytes): Dictionary path for MeCab userdic.
                This option is ignored when empty bytestring is given.
                Default is empty.
        """
        pass
    def run_frontend(self, text: str | bytes | bytearray) -> list[_NJDFeature]:
        """Run OpenJTalk's text processing frontend"""
        pass
    def make_label(self, features: Iterable[Mapping]) -> list[str]:
        """Make full-context label"""
        pass
    @overload
    def g2p(
        self,
        text: str | bytes | bytearray,
        kana: bool = ...,
        join: Literal[False] = ...,
    ) -> list[str]: ...
    @overload
    def g2p(
        self, text: str | bytes | bytearray, kana: bool = ..., join: Literal[True] = ...
    ) -> str: ...
    @overload
    def g2p(
        self, text: str | bytes | bytearray, kana: bool = False, join: bool = True
    ) -> list[str] | str:
        """Grapheme-to-phoeneme (G2P) conversion"""
        pass

def mecab_dict_index(dn_mecab: bytes, path: bytes, out_path: bytes) -> int: ...

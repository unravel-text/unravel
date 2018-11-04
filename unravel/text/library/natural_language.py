from io import TextIOBase

from unravel.text.text_info import TextInfo


class NaturalLanguage:
    def get_text_info(self, text: str) -> TextInfo:
        raise NotImplementedError()

    def get_text_info_stream(self, text_stream: TextIOBase) -> TextInfo:
        raise NotImplementedError()
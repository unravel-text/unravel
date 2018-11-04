from logging import Logger


from unravel.text import ReadingLevel
from unravel.text.library import NaturalLanguage


class BaseReadability:
    def __init__(self, logger: Logger, text_analyser: NaturalLanguage):
        self._logger = logger
        self._text_analyser = text_analyser

    def calc(self, text: str) -> ReadingLevel:
        """
        Calculate the readability metric on text.
        Return an estimate of the number of years of
        education required to understand the text.
        """

        raise NotImplementedError()

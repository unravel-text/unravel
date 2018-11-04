from logging import Logger


from unravel.text import ReadingLevel
from unravel.text.natural_language import NaturalLanguage


class BaseReadability:
    def __init__(self, logger: Logger, nl: NaturalLanguage):
        self._nl = nl
        self._logger = logger

    def calc(self, text: str) -> ReadingLevel:
        """
        Calculate the readability metric on text.
        Return an estimate of the number of years of
        education required to understand the text.
        """

        raise NotImplementedError()

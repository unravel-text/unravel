from math import sqrt

from unravel.text.readability import BaseReadability
from unravel.text import ReadingLevel


class SimpleMeasureOfGobbledygook(BaseReadability):
    """
    The SMOG grade is a measure of readability that estimates the years of education needed to understand a
    piece of writing. It gives the estimated grade required to fully understand a piece of text.
    SMOG is an acronym for Simple Measure of Gobbledygook.
    SMOG is widely used, particularly for checking health messages.

    Description from https://en.wikipedia.org/wiki/SMOG

    0.4 x ((total words / total sentences) + 100 * (total complex words / total words))
    """

    name = 'Simple Measure of Gobbledygook'
    slug = 'simple_measure_of_gobbledygook'

    def calc(self, text: str) -> ReadingLevel:
        if not text:
            return ReadingLevel(self.name)
        text_info = self._nl.get_text_info(text)
        sentences = text_info.sentence_count
        polysyllable_words = text_info.polysyllable_word_count

        if sentences < 1:
            return ReadingLevel(self.name, text_info)

        if sentences < 30:
            self._logger.warning('Calculating SMOG readability on text with fewer '
                                 'than 30 sentences ({})'.format(sentences))

        result = 1.0430 * sqrt(polysyllable_words * 30.0 / sentences) + 3.1291
        if result < 0:
            result = 0
        reading = ReadingLevel(self.name, text_info, index=result, level=int(result), age=int(result) + 4)
        return reading

from unravel.text.readability import BaseReadability
from unravel.text import ReadingLevel


class LinsearWrite(BaseReadability):
    """
    Linsear Write is a readability metric for English text, purportedly developed for the United States Air Force to
    help them calculate the readability of their technical manuals. It is one of many such readability metrics, but
    is specifically designed to calculate the United States grade level of a text sample based on sentence length and
    the number of words used that have three or more syllables.

    Description from https://en.wikipedia.org/wiki/Linsear_Write

    - Find a 100-word sample from your writing.
    - Calculate the easy words (defined as two syllables or less) and
      place a number "1" over each word, even including a, an, the, and other simple words.
    - Calculate the hard words (defined as three syllables or more) and
      place a number "3" over each word as pronounced by the dictionary.
    - Multiply the number of easy words times "1."
    - Multiply the number of hard words times "3."
    - Add the two previous numbers together.
    - Divide that total by the number of sentences.
    - If your answer is >20, divide by "2," and that is your answer.
    - If your answer is <20 or equal to 20, subtract "2," and then divide by "2." That is your answer.

    """

    name = 'Linsear Write'
    slug = 'linsear_write'

    def calc(self, text: str) -> ReadingLevel:
        if not text:
            return ReadingLevel(self.name)
        text_info = self._nl.get_text_info(text)
        words = text_info.word_count
        sentences = text_info.sentence_count

        if words < 100:
            self._logger.warning('Calculating Linsear Write on fewer than 100 words ({})'.format(words))

        easy_word_score = text_info.word_syllable_count(min_count=0, max_count=2)
        hard_word_score = text_info.word_syllable_count(min_count=3) * 3

        raw_result = (easy_word_score + hard_word_score) / sentences
        if raw_result > 20:
            result = raw_result / 2
        else:
            result = (raw_result - 2) / 2

        if result < 0:
            result = 0
        reading = ReadingLevel(self.name, text_info, index=result, level=int(result), age=int(result) + 4)
        return reading

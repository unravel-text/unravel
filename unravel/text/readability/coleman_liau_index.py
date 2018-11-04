from unravel.text.readability import BaseReadability
from unravel.text import ReadingLevel


class ColemanLiauIndex(BaseReadability):
    """
    Approximates the U.S. grade level thought necessary to comprehend the text.

    U.S. grade levels are 1 through 12.

    Description from https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index

    0.0588 x L - 0.296 x S - 15.8

    L is the average number of letters per 100 words and S is the average number of sentences per 100 words.
    """

    name = 'Coleman-Liau Index'
    slug = 'coleman_liau_index'

    def calc(self, text: str) -> ReadingLevel:
        if not text:
            return ReadingLevel(self.name)

        text_info = self._nl.get_text_info(text)
        characters = text_info.character_count
        words = text_info.word_count
        sentences = text_info.sentence_count

        if sentences < 1 or words < 1:
            return ReadingLevel(self.name, text_info)

        ave_letters = (characters / words) * 100
        ave_sentences = (sentences / words) * 100

        result = (0.0588 * ave_letters) - (0.296 * ave_sentences) - 15.8
        if result < 0:
            result = 0
        reading = ReadingLevel(self.name, text_info, index=result, level=int(result), age=int(result) + 4)
        return reading

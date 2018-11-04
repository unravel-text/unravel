from unravel.text.readability import BaseReadability
from unravel.text import ReadingLevel


class FleschKincaidGradeLevel(BaseReadability):
    """
    Presents a score as a U.S. grade level. It can also mean the number of years of education generally
    required to understand this text, relevant when the formula results in a number greater than 10.

    U.S. grade levels are 1 through 12.

    Description from https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch.E2.80.93Kincaid_grade_level

    0.39 x (total words / total sentences) + 11.8 x (total syllables / total words) - 15.59
    """

    name = 'Flesch-Kincaid grade level'
    slug = 'flesch_kincaid_grade_level'

    def calc(self, text: str) -> ReadingLevel:
        if not text:
            return ReadingLevel(self.name)

        text_info = self._text_analyser.get_text_info(text)
        words = text_info.word_count
        sentences = text_info.sentence_count
        syllables = text_info.syllable_count

        if sentences < 1 or words < 1:
            return ReadingLevel(self.name)

        result = 0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59
        if result < 0:
            result = 0
        reading = ReadingLevel(self.name, index=result, level=int(result), age=int(result) + 4)
        return reading

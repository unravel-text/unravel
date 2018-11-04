from unravel.text.readability import BaseReadability
from unravel.text import ReadingLevel


class FleschReadingEase(BaseReadability):
    """
    In the Flesch reading-ease test, higher scores indicate material that is easier to read;
    lower numbers mark passages that are more difficult to read.

    100.00-90.00    5th grade           Very easy to read. Easily understood by an average 11-year-old student.
    90.0–80.0       6th grade           Easy to read. Conversational English for consumers.
    80.0–70.0       7th grade           Fairly easy to read.
    70.0–60.0       8th & 9th grade     Plain English. Easily understood by 13- to 15-year-old students.
    60.0–50.0       10th to 12th grade  Fairly difficult to read.
    50.0–30.0       College             Difficult to read.
    30.0–0.0        College graduate    Very difficult to read. Best understood by university graduates.
    
    Description from https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch_reading_ease

    206.835 - 1.015 x (total words / total sentences) - 84.6 x (total syllables / total words)
    """

    name = 'Flesch reading ease'
    slug = 'flesch_reading_ease'

    def calc(self, text: str) -> ReadingLevel:
        if not text:
            return ReadingLevel(self.name)
        text_info = self._nl.get_text_info(text)
        words = text_info.word_count
        sentences = text_info.sentence_count
        syllables = text_info.syllable_count

        if sentences < 1 or words < 1:
            return ReadingLevel(self.name, text_info)

        result = 206.835 - 1.015 * (words / sentences) - 85.6 * (syllables / words)

        if result > 130.0:
            level = 1
        elif result > 120.0:  # this is made up
            level = 2
        elif result > 110.0:  # this is made up
            level = 3
        elif result > 100.0:  # this is made up
            level = 4
        elif result > 90.0:
            level = 5
        elif result > 80.0:
            level = 6
        elif result > 70.0:
            level = 7
        elif result > 65.0:  # this is made up
            level = 8
        elif result > 60.0:
            level = 9
        elif result > 53.33:  # this is made up
            level = 10
        elif result > 56.66:  # this is made up
            level = 11
        elif result > 50.0:
            level = 12
        elif result > 45.0:  # this is made up
            level = 13
        elif result > 40.0:  # this is made up
            level = 14
        elif result > 35.0:  # this is made up
            level = 15
        elif result > 30.0:  # this is made up
            level = 16
        elif result > 15.0:  # this is made up
            level = 17
        else:  # this is made up
            level = 18

        reading = ReadingLevel(self.name, text_info, index=result, level=level)
        return reading

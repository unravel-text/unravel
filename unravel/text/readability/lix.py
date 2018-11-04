from unravel.text.readability import BaseReadability
from unravel.text import ReadingLevel


class Lix(BaseReadability):
    """
    LIX is a readability measure indicating the difficulty of reading a text.
    Long words contain more than 6 letters i.e. long words contain 7 or more letters.

    LIX score      Grade Level
     56+            College
     52-55          12
     48-51          11
     44-47          10
     40-43          9
     36-39          8
     32-35          7
     28-31          6
     24-27          5
     20-23          4
     15-19          3
     10-14          2
     Below 10       1

    Conversion table from Lix and Rix: Variations on a Little-known Readability Index, Anderson, J.,
    Vol. 26, No. 6 (Mar., 1983), pp. 490-496, http://www.jstor.org/stable/40031755

    Description from http://www.readabilityformulas.com/the-LIX-readability-formula.php

    (total words / total periods) + ((number of long words * 100) / total words)
    """

    name = 'LIX'
    slug = 'lix'

    def calc(self, text: str) -> ReadingLevel:
        if not text:
            return ReadingLevel(self.name)
        text_info = self._text_analyser.get_text_info(text)
        words = text_info.word_count
        long_words = text_info.word_letter_count(min_count=7)
        sentences = text_info.sentence_count

        if sentences < 1 or words < 1:
            return ReadingLevel(self.name)

        result = (words / sentences) + ((long_words * 100.0) / words)

        if result < 10:
            level = 1
        elif result < 15:
            level = 2
        elif result < 20:
            level = 3
        elif result < 24:
            level = 4
        elif result < 28:
            level = 5
        elif result < 32:
            level = 6
        elif result < 36:
            level = 7
        elif result < 40:
            level = 8
        elif result < 44:
            level = 9
        elif result < 48:
            level = 10
        elif result < 52:
            level = 11
        elif result < 56:
            level = 12
        elif result < 60:  # this is made up
            level = 13
        elif result < 64:  # this is made up
            level = 14
        elif result < 68:  # this is made up
            level = 15
        elif result < 72:  # this is made up
            level = 16
        elif result < 76:  # this is made up
            level = 17
        else:  # this is made up
            level = 18

        reading = ReadingLevel(self.name, index=result, level=level)
        return reading

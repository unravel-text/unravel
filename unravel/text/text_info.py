class TextInfo:

    def __init__(self, *args, **kwargs):
        self._values = {}
        if kwargs:
            for name, value in kwargs.items():
                if hasattr(self, name):
                    self._values[name] = value
                else:
                    raise ValueError('Invalid value for TextInfo "{}":{}'.format(name, value))

    @property
    def character_count(self):
        return self._values.get('character_count')

    @property
    def word_count(self):
        return self._values.get('word_count')

    @property
    def sentence_count(self):
        return self._values.get('sentence_count')

    @property
    def syllable_count(self):
        return self._values.get('syllable_count')

    @property
    def polysyllable_word_count(self):
        return self._values.get('polysyllable_word_count')

    @property
    def words(self):
        return self._values.get('words')

    @property
    def data(self):
        return self._values.get('data')

    def word_letter_count(self, min_count: int = None, max_count: int = None) -> int:
        """Count the number of words that contain at least min_count letters,
        up to and including max_count letters."""

        matches = []
        for i in self._values['data']:
            matches_min = min_count is not None and i['letter_count'] >= min_count
            matches_max = max_count is not None and i['letter_count'] <= max_count

            if (min_count is None or matches_min) and (max_count is None or matches_max):
                matches.append(i)

        return len(matches)

    def word_syllable_count(self, min_count: int = None, max_count: int = None) -> int:
        """Count the number of words that contain at least min_count syllables,
        up to and including max_count syllables."""

        matches = []
        for i in self._values['data']:
            matches_min = min_count is not None and i['syllable_count1'] >= min_count
            matches_max = max_count is not None and i['syllable_count1'] <= max_count

            if (min_count is None or matches_min) and (max_count is None or matches_max):
                matches.append(i)

        return len(matches)



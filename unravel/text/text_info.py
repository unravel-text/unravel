class TextInfo:

    def __init__(self, *args, **kwargs):
        self._values = {}
        if kwargs:
            for name, value in kwargs.items():
                if hasattr(self, name):
                    self._values[name] = value
                else:
                    raise ValueError('Invalid value for TextInfo {}:{}'.format(name, value))

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
    def polysyllable_count(self):
        return self._values.get('polysyllable_count')

    def word_letter_count(self, min_count: int = None, max_count: int = None) -> int:
        """Count the number of words that contain at least min_count letters,
        up to and including max_count letters."""
        raise NotImplementedError()

    def word_syllable_count(self, min_count: int = None, max_count: int = None) -> int:
        """Count the number of words that contain at least min_count syllables,
        up to and including max_count syllables."""
        raise NotImplementedError()

    def _count_syllables(self, word: str):
        # see https://stackoverflow.com/questions/405161/detecting-syllables-in-a-word#405179
        # could also use pyphen
        vowels = "aeiouy"
        num_vowels = 0
        last_was_vowel = False
        for wc in word:
            found_vowel = False
            for v in vowels:
                # don't count diphthongs
                if v == wc and last_was_vowel:
                    found_vowel = True
                    last_was_vowel = True
                    break
                elif v == wc and not last_was_vowel:
                    num_vowels += 1
                    found_vowel = True
                    last_was_vowel = True
                    break
            # If full cycle and no vowel found, set lastWasVowel to false
            if not found_vowel:
                last_was_vowel = False
        # Remove es - it's "usually" silent (?)
        if len(word) > 2 and word[-2:] == "es":
            num_vowels -= 1
        # remove silent e
        elif len(word) > 1 and word[-1:] == "e":
            num_vowels -= 1
        return num_vowels

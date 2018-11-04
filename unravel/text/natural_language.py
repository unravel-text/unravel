import pyphen
import spacy
from unravel.text.text_info import TextInfo


class NaturalLanguage:

    def __init__(self):
        self.tool_spacy = spacy.load('en_core_web_sm')
        self.tool_pyphen = pyphen.Pyphen(lang='en_GB')

    def get_text_info(self, text: str) -> TextInfo:
        character_count = len(text)

        spacy_doc = self.tool_spacy(text)
        sentences = list(spacy_doc.sents)
        words = []
        text_info_data = []
        for token in spacy_doc:

            if not token.is_punct and not token.is_space:
                syllables = list(self.tool_pyphen.iterate(token.text))
                syllables_2 = self._simple_syllables_count(token.text)
                words.append((token, syllables))
            else:
                syllables = None
                syllables_2 = 0

            text_info_data.append({
                'token': token,
                'syllables': syllables,
                'sentence_id': [index for index, i in enumerate(sentences) if token.sent.text == i.text][0],
                'letter_count': len(token.text),
                'syllable_count1': len(syllables) + 1 if syllables is not None else 0,
                'syllable_count2': syllables_2,
            })

        word_count = len(words)
        sentence_count = len(list(spacy_doc.sents))
        syllable_count = len([s for w in words for s in w[1]])
        polysyllable_word_count = len([w for w in words if len(w[1]) > 1])

        text_info = TextInfo(
            character_count=character_count,
            word_count=word_count,
            sentence_count=sentence_count,
            syllable_count=syllable_count,
            polysyllable_word_count=polysyllable_word_count,
            words=[w[0].text for w in words],
            data=text_info_data
        )
        return text_info

    def _simple_syllables_count(self, word: str):
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

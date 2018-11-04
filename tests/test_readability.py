import logging

import nltk
import pyphen
import spacy
from unittest import TestCase

from unravel.text import TextInfo

from unravel.text.natural_language import NaturalLanguage
from unravel.text.readability import AutomatedReadabilityIndex, ColemanLiauIndex, DaleChallReadabilityFormula, \
    FleschKincaidGradeLevel, FleschReadingEase, GunningFogIndex, LinsearWrite, Lix, Rix, SimpleMeasureOfGobbledygook


class ReadabilityTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.logger = logging.getLogger('test')
        cls.sample_text = [
            {'text': "Existing computer programs that measure readability are based largely upon subroutines which "
                     "estimate number of syllables, usually by counting vowels. The shortcoming in estimating syllables "
                     "is that it necessitates keypunching the prose into the computer. There is no need to estimate "
                     "syllables since word  length in letters is a better predictor of readability than word length in "
                     "syllables. Therefore, a new readability formula was computed that has for its predictors letters "
                     "per 100 words and sentences  per 100 words. Both predictors can be counted by an optical scanning "
                     "device, and thus the formula makes it economically feasible for an organization such as the U.S. "
                     "Office of Education to calibrate the readability of all textbooks for the public school system.",
             'chars': 769, 'sentences': 5, 'words': 119, 'level': 14.5},
            {'text': "The Australian platypus is seemingly a hybrid of a mammal and reptilian creature.",
             'chars': 81, 'sentences': 1, 'words': 13, 'syllables': 24, 'level': 11.3}
        ]

    def test_readability(self):
        nl = NaturalLanguage()
        ris = [
            AutomatedReadabilityIndex(self.logger, nl),
            ColemanLiauIndex(self.logger, nl),
            DaleChallReadabilityFormula(self.logger, nl),
            FleschKincaidGradeLevel(self.logger, nl),
            FleschReadingEase(self.logger, nl),
            GunningFogIndex(self.logger, nl),
            LinsearWrite(self.logger, nl),
            Lix(self.logger, nl),
            Rix(self.logger, nl),
            SimpleMeasureOfGobbledygook(self.logger, nl),
        ]

        for ri in ris:
            for sample in self.sample_text:
                with self.subTest(sample=sample['text'][0:10], ri=ri.slug):
                    reading_level = ri.calc(sample['text'])
                    self.assertEqual(reading_level.text_info.character_count, sample['chars'])
                    self.assertEqual(reading_level.text_info.sentence_count, sample['sentences'])
                    self.assertEqual(reading_level.text_info.word_count, sample['words'])

                    self.assertAlmostEqual(reading_level.level, sample['level'], delta=1.5)

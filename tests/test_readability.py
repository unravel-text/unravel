import logging
from unittest import TestCase

from unravel.text.library import NltkNaturalLanguage, SpacyNaturalLanguage
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
             'chars': 639, 'sentences': 5, 'words': 119, 'level': 14.5},
            {'text': "The Australian platypus is seemingly a hybrid of a mammal and reptilian creature.",
             'chars': 68, 'sentences': 1, 'words': 13, 'syllables': 24, 'level': 11.3}
        ]

    def test_nltk(self):
        nltk = NltkNaturalLanguage()
        ris = [
            AutomatedReadabilityIndex(self.logger, nltk),
            ColemanLiauIndex(self.logger, nltk),
            DaleChallReadabilityFormula(self.logger, nltk),
            FleschKincaidGradeLevel(self.logger, nltk),
            FleschReadingEase(self.logger, nltk),
            GunningFogIndex(self.logger, nltk),
            LinsearWrite(self.logger, nltk),
            Lix(self.logger, nltk),
            Rix(self.logger, nltk),
            SimpleMeasureOfGobbledygook(self.logger, nltk),
        ]

        for ri in ris:
            for sample in self.sample_text:
                with self.subTest(sample=sample):
                    reading_level = ri.calc(sample['text'])
                    self.assertEqual(reading_level.level, sample['level'])

    def test_spacy(self):
        spacy = SpacyNaturalLanguage()

        ris = [
            AutomatedReadabilityIndex(self.logger, spacy),
            ColemanLiauIndex(self.logger, spacy),
            DaleChallReadabilityFormula(self.logger, spacy),
            FleschKincaidGradeLevel(self.logger, spacy),
            FleschReadingEase(self.logger, spacy),
            GunningFogIndex(self.logger, spacy),
            LinsearWrite(self.logger, spacy),
            Lix(self.logger, spacy),
            Rix(self.logger, spacy),
            SimpleMeasureOfGobbledygook(self.logger, spacy),
        ]

        for ri in ris:
            for sample in self.sample_text:
                with self.subTest(sample=sample):
                    reading_level = ri.calc(sample['text'])
                    self.assertEqual(reading_level.level, sample['level'])

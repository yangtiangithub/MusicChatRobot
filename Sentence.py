from LtpUtil import LtpUtil
from KeywordUtil import KeyworsUtil
class Sentence(object):
    def __init__(self,sentence):
        self.sentence = sentence
        self.ltpUtil = LtpUtil()
        self.words = list(self.ltpUtil.Segmentor(sentence))
        self.postags = list(self.ltpUtil.Postagger_with_words(self.words))
        self.netags = list(self.ltpUtil.NamedEntityRecognizer_with_wordsAndPostags(self.words, self.postags))
        self.arcs = self.ltpUtil.Parser_with_wordsAndPostags(self.words, self.postags)

        self.keywordUtil = KeyworsUtil()
        self.personName_nums,self.personNames = self.keywordUtil.getPersonName(self.words,self.postags)
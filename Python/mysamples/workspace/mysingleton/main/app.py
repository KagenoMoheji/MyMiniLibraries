import inspect
import os
import sys
PYPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
ROOTPATH = "{}/.".format(PYPATH)
sys.path.append(ROOTPATH)

import pandas as pd

from modules.myutils.mysingleton import Singleton

class JanomeTokenizer(Singleton):
    tokenizer = None

    def _init_instance(self, udic = None, udic_type = "ipadic"):
        JanomeTokenizer.tokenizer = JanomeTokenizer._create_tokenizer(udic, udic_type)
    
    def _create_tokenizer(udic = None, udic_type = "ipadic"):
        from janome.tokenizer import Tokenizer
        t = None
        if udic is None:
            t = Tokenizer()
        else:
            t = Tokenizer(udic, udic_type = udic_type, udic_enc = "utf8")
        return t

    @staticmethod
    def str_joined_tokenize(s, list_stopword = [], sep = "|"):
        tokens = JanomeTokenizer.tokenize(s, list_stopword = list_stopword)
        return sep.join([token.surface for token in tokens])
    
    @staticmethod
    def tokenize(s, list_stopword = []):
        return JanomeTokenizer.__remove_stopwords(
            JanomeTokenizer.tokenizer.tokenize(s),
            list_stopword = list_stopword
        )
    
    @staticmethod
    def __remove_stopwords(tokens, list_stopword = []):
        new_tokens = []
        for token in tokens:
            if "記号,空白,*,*" in token.part_of_speech:
                continue
            if "記号,括弧開,*,*" in token.part_of_speech:
                continue
            if "記号,括弧閉,*,*" in token.part_of_speech:
                continue
            if "助詞,連体化,*,*" in token.part_of_speech:
                continue
            if token.surface in list_stopword:
                continue
            new_tokens.append(token)
        return new_tokens

def addcol_str_joined_tokenize(df, target_cols, udic = None, udic_type = "ipadic", list_stopword = [], sep = "|"):
    def __apply_tokenize(field):
        return JanomeTokenizer(udic = udic, udic_type = udic_type) \
                    .str_joined_tokenize(field, list_stopword = list_stopword, sep = sep)
    for target_col in target_cols:
        colname_joined_tokens = "tokens_" + target_col
        df[colname_joined_tokens] = df[target_col].apply(__apply_tokenize)
    return df

list_s = [
    "こんにちは，私の名前はもへじです．",
    "今夜は月が綺麗ですね．",
    "明日も残業かなぁ？"
]
df = pd.DataFrame(list_s, columns = ["sentence"])
options = {
    "udic": None,
    "udic_type": "ipadic",
    "list_stopword": ["．", "，"],
    "sep": "|"
}
df = addcol_str_joined_tokenize(df, ["sentence"], **options)
print(df)
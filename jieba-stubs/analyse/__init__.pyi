from .tfidf import TFIDF
from .textrank import TextRank

default_tfidf: TFIDF
default_textrank: TextRank

extract_tags = tfidf = default_tfidf.extract_tags
set_idf_path = default_tfidf.set_idf_path
textrank = default_textrank.extract_tags


def set_stop_words(stop_words_path: str) -> None:
    ...

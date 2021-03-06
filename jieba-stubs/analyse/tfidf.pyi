from typing import Dict, List, Set, Tuple
from jieba import Tokenizer
from jieba.posseg import POSTokenizer

DEFAULT_IDF: str


class KeywordExtractor:
    STOP_WORDS: Set[str]

    def set_stop_words(self, stop_words_path: str) -> None:
        ...

    def extract_tags(self, *args, **kwargs) -> None:
        ...


class IDFLoader(object):
    path: str
    idf_freq: Dict[str, float]
    median_idf: float

    def __init__(self, idf_path: str | None = ...) -> None:
        ...

    def set_new_path(self, new_idf_path: str) -> None:
        ...

    def get_idf(self) -> Tuple[Dict[str, float], float]:
        ...


class TFIDF(KeywordExtractor):
    tokenizer: Tokenizer
    postokenizer: POSTokenizer
    stop_words: Set[str]
    idf_loader: IDFLoader
    idf_freq: Dict[str, float]
    median_idf: float

    def __init__(self, idf_path: str | None = ...) -> None:
        ...

    def set_idf_path(self, idf_path: str) -> None:
        ...

    def extract_tags(
        self,
        sentence: str,
        topK: int = ...,
        withWeight: bool = ...,
        allowPOS: Tuple[str, ...] = ...,
        withFlag: bool = ...,
    ) -> List[Tuple[str, float] | str]:
        ...

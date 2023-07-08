import functools
from dataclasses import dataclass
import re

from texts.models import Word


def return_text(text: str):
    return "".join(
        token.render() for token in tokenize(text)
    )


@dataclass
class TextToken:
    text: str
    attr_class: str
    progress: str

    def render(self) -> str:
        progress = (" " if self.progress else '') + self.progress
        return f"<span class=\"word word_{self.attr_class}{progress}\">{self.text}</span>"


@dataclass
class SymbolToken:
    symbol: str

    def render(self) -> str:
        return self.symbol


def tokenize(txt: str) -> list[TextToken | SymbolToken]:
    split_string = re.findall(r'\w+|\W+', txt)

    @functools.cache
    def get_word_status(word: str) -> str:
        result = Word.objects.filter(word=word)
        return result[0].progress if result else ""

    def create_token(chunk):
        if chunk.isalpha():
            return TextToken(chunk, chunk.lower(), get_word_status(chunk.lower()))
        return SymbolToken(chunk)

    return [create_token(chunk) for chunk in split_string]



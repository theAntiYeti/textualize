import re
from dataclasses import dataclass

from django.http import HttpResponse
from django.shortcuts import render

# TODO: should come from database.
text = "This is a text made that should be tokenized and returned as HTML. I am adding some more words. this text Text."


# Create your views here.
def return_text(request):
    return HttpResponse("".join(
        token.render() for token in tokenize(text)
    ))


@dataclass
class TextToken:
    text: str
    attr_class: str

    def render(self) -> str:
        return f"<span class=\"word word_{self.attr_class}\">{self.text}</span>"


@dataclass
class SymbolToken:
    symbol: str

    def render(self) -> str:
        return self.symbol


def tokenize(txt: str) -> list[TextToken | SymbolToken]:
    split_string = re.findall(r'\w+|\W+', txt)

    def create_token(chunk):
        if chunk.isalpha():
            return TextToken(chunk, chunk.lower())
        return SymbolToken(chunk)

    return [create_token(chunk) for chunk in split_string]


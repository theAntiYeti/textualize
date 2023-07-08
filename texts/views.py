from django.http import HttpResponse, HttpResponseBadRequest

from texts.models import Text, Word
from texts.src.return_text import return_text


def serve_text(request):
    text_id = request.GET["id"]
    text = Text.objects.get(pk=text_id).text

    return HttpResponse(
        return_text(text)
    )


def update_word(request, word: str):
    if "progress" not in request.GET:
        return update_word_delete(word)
    else:
        return update_word_put(word, request.GET["progress"])


def update_word_delete(word):
    Word.objects.filter(word=word).delete()
    return HttpResponse(f'Word deleted')


def update_word_put(word, progress):
    if progress not in {'new', 'learning', 'learned'}:
        return HttpResponseBadRequest(f'Progress {progress} invalid.')

    results = Word.objects.filter(word=word)

    if not results:
        Word(word=word, progress=progress).save()
        return HttpResponse(f'New word {word} saved')

    found_word = results[0]
    found_word.progress = progress
    found_word.save()
    return HttpResponse(f'Found word {word} updated')

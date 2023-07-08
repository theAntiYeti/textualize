from django.shortcuts import render

from texts.models import Text


# Create your views here.


def textview(request):
    text_id = request.GET["id"]
    title = Text.objects.get(id=text_id).title
    return render(request, "textview/display_text.html", {"text_id": text_id, "title": title})


def sidebar(request):
    word_class = request.GET["word_class"]
    return render(request, "textview/sidebar.html", {"word_class": word_class})
from django.shortcuts import render

# Create your views here.


def textview(request):
    text_id = request.GET["id"]
    return render(request, "textview/display_text.html", { "text_id": text_id})


def sidebar(request):
    word_class = request.GET["word_class"]
    return render(request, "textview/sidebar.html", {"word_class": word_class})
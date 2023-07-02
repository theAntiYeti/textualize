from django.shortcuts import render

# Create your views here.


def textview(request):
    return render(request, "textview/display_text.html")


def sidebar(request):
    word_class = request.GET["word_class"]
    return render(request, "textview/sidebar.html", {"word_class": word_class})
from django.shortcuts import render

# Create your views here.


def textview(request):
    return render(request, "display_text.html")
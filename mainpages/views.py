from django.shortcuts import render

from texts.models import Text


# Create your views here.
def selection_page(request):
    texts = Text.objects.all()
    print(texts)
    return render(request, "selection_page/selection_page.html", {"texts": texts})

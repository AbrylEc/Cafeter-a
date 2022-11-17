from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.


def sample(request, pageId):
    page = get_object_or_404(Page, id=pageId)
    return render(request, "page/sample.html", {'page': page})

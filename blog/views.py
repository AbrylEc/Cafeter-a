from django.shortcuts import render, get_object_or_404
from .models import Blog, Category

# Create your views here.


def blog(request):
    blogs = Blog.objects.all()  # Equivaldría a un select .all
    return render(request, "blog/blog.html", {'blogs': blogs})


# Vista para ver las entradas por cada categoría
def category(request, categoryId):
    category = get_object_or_404(Category, id=categoryId)
    # Filtrar las entradas enlazadas a esa categoría
    blogs = Blog.objects.filter(categories=category)
    #category = Category.objects.get(id=categoryId)
    # return render(request, "blog/category.html", {'category': category, 'blogs': blogs})
    return render(request, "blog/category.html", {'category': category})

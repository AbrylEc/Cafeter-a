from django.contrib import admin

from .models import Category, Blog

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # Publicar columnas -> esto lo estamos trayendo del modelo
    list_display = ('title', 'author', 'published')
    # Se coloca la coma aunque solo estè 'author',
    ordering = ('author', 'published')
    # Buscador
    # Es doble guión bajo
    search_fields = ('title', 'content',
                     'author__username', 'categories__name')
    # Navegación por fechas
    date_hierarchy = 'published'

    # Añadir filtro
    list_filter = ('author__username',)


# Gestionar desde al administrador
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)

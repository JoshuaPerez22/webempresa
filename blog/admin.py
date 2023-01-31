from django.contrib import admin
from .models import Category, Post

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # Campos que se muestran en la lista
    list_display = ('title', 'author', 'published', 'post_categories',)
    # Ordenar por...
    ordering = ('author', 'published',)
    # Buscar por...
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    # Jerarquía de fechas
    date_hierarchy = 'published'
    # Filtros que aparecen en el panel de la derecha
    list_filter = ('author__username', 'categories__name')

    # Método para mostrar las categorías (Usado en list_display, línea 14)
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description = 'Categorías'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Última actualización', auto_now=True)

    class Meta:
        verbose_name = 'categoría'
        ordering = ['-created']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=timezone.now())
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Categorías', related_name='get_posts')
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Última actualización', auto_now=True)

    class Meta:
        verbose_name = 'entrada'
        ordering = ['-created']

    def __str__(self):
        return self.title

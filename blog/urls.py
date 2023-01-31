from django.urls import path
from . import views as blog_views

app_name = 'blog'

urlpatterns = [
    path('', blog_views.blog, name='blog'),
    path('category/<int:category_id>/', blog_views.category, name='category'),
]
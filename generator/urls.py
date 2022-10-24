from django.urls import path
from .views import generator_view, pass_view, about_view

urlpatterns = [
    path('', generator_view, name='generator'),
    path('password', pass_view, name='password'),
    path('about/', about_view, name='about'),
]
from django.urls import URLPattern, path, include
from .views import index

urlpatterns = [
    path('', index, name='home')
]
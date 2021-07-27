from django.urls import path

from books.views import HomeTemplateView

app_name = 'books'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home')
]
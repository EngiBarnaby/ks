from django.urls import path

from .views import WordList


urlpatterns = [
    path("word-list/", WordList.as_view(), name="word-list")
]
from django.urls import path

from .views import WordList, WordListTest


urlpatterns = [
    path("words-list/", WordList.as_view(), name="word-list"),
    path("words-list-test/", WordListTest.as_view(), name="word-list") 
]
from django.urls import path

from .views import WordList, WordListTest, WordTranslateList


urlpatterns = [
    path("words-list/", WordList.as_view(), name="word-list"),
    path("words-list-test/", WordListTest.as_view(), name="word-list"),
    path("word-translate-list/", WordTranslateList.as_view(), name="word-translate-list")
]
from django.db import models
from django.conf import settings


CHOICES = (
        ("noun", "noun"),
        ("pronoun", "pronoun"),
        ("verb", "verb"),
        ("adjective", "adjective"),
        ("adverb", "adverb"),
        ("preposition", "preposition"),
        ("conjunction.", "conjunction"),
        ("interjection", "interjection"),
    )


class Word(models.Model):

    CHOICES_LANG = (
        ("rus", "Russian"),
        ("eng", "English"),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                            on_delete=models.CASCADE,
                            related_name="words" )
    content = models.CharField(max_length=50, null=False, blank=False)
    # part_of_speech = models.CharField(max_length=50, choices=CHOICES)
    language = models.CharField(max_length=50, choices=CHOICES_LANG)
    create_at = models.DateField(auto_now_add=True) 
    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.content


class WordTranslate(models.Model):
    translate = models.CharField(max_length=50, blank=False, null=False)
    part_of_speech = models.CharField(max_length=50, choices=CHOICES)
    word = models.ForeignKey(Word, on_delete=models.CASCADE,
                            related_name="words_translate")

    def __str__(self):
        return self.translate
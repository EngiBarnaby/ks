from django.db import models
from django.conf import settings

class Word(models.Model):
    CHOICES = (
        ("n.", "NOUN"),
        ("pro.", "PRONOUN"),
        ("v.", "VERB"),
        ("adj.", "ADJECTIVE"),
        ("adv.", "ADVERB"),
        ("pre.", "PREPOSITION"),
        ("con.", "CONJUNCTION"),
        ("int.", "INTERJECTION"),
    )

    CHOICES_LANG = (
        ("rus", "Russian"),
        ("eng", "English"),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                            on_delete=models.CASCADE,
                            related_name="words" )
    content = models.CharField(max_length=50, null=False, blank=False)
    part_of_speech = models.CharField(max_length=50, choices=CHOICES)
    language = models.CharField(max_length=50, choices=CHOICES_LANG)
    create_at = models.DateField(auto_now_add=True) 
    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.content


class WordTranslate(models.Model):
    translate = models.CharField(max_length=50, blank=False, null=False)
    word = models.ForeignKey(Word, on_delete=models.CASCADE,
                            related_name="words_translate")

    def __str__(self):
        return self.translate
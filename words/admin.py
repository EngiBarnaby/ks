from django.contrib import admin

from .models import Word, WordTranslate


admin.site.register(Word)
admin.site.register(WordTranslate)
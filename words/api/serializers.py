from django.db.models import fields
from rest_framework import serializers

from ..models import Word, WordTranslate

class WordTranslateSerializer(serializers.ModelSerializer):

    class Meta:
        model = WordTranslate
        fields = "__all__"


class WordSerializer(serializers.ModelSerializer):
    
    words_translate = WordTranslateSerializer(many=True, read_only=True)

    class Meta:
        model = Word
        fields = "__all__"


from rest_framework import generics

from .serializers import WordSerializer
from ..models import Word

class WordList(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def get_queryset(self):
        user = self.request.user
        words = Word.objects.filter(user=user)
        return words

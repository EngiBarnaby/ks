from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated

from .serializers import WordSerializer, WordTranslateSerializer
from ..models import Word, WordTranslate

class WordList(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        words = Word.objects.filter(user=user)
        return words

class WordListTest(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [IsAuthenticated]


class WordTranslateList(generics.ListCreateAPIView):
    queryset = WordTranslate.objects.all()
    serializer_class = WordTranslateSerializer


from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

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

class WordsPagination(PageNumberPagination):
        page_size = 15
        max_page_size = 50
        page_size_query_param = "page_size"

class WordListTest(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = WordsPagination


class WordTranslateList(generics.ListCreateAPIView):
    queryset = WordTranslate.objects.all()
    serializer_class = WordTranslateSerializer


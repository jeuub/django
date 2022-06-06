from rest_framework.viewsets import ModelViewSet
from .serializers import QuizSerializer, AuthorsSerializer, CategotiesSerializer
from .models import Quiz, Authors, Categoties
from rest_framework.generics import ListAPIView 
import django_filters.rest_framework
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response


class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class GetQuizView(ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['votes_for','creator']


class CategotiesViewSet(ModelViewSet):
    queryset = Categoties.objects.all()
    serializer_class = CategotiesSerializer

class GetCategotiesView(ListAPIView):
    queryset = Categoties.objects.filter( Q(reviews__gt=5) | Q(name = 'Фильмы'))
    serializer_class = CategotiesSerializer

class AuthorsViewSet(ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    @action(methods=['Delete'], detail=True, url_path='delete') 
    def delAutor(self,request, pk=None):
        author=self.queryset.get(id=pk)
        author.delete()
        return Response('Succses')
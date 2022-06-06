from rest_framework.serializers import ModelSerializer
from .models import Quiz, Categoties, Authors


class QuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class CategotiesSerializer(ModelSerializer):
    class Meta:
        model = Categoties
        fields = '__all__'

class AuthorsSerializer(ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'
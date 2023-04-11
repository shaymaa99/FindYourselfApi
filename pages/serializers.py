from rest_framework import serializers
from .models import Book,Activity,Category,Video,app_Question,Data_of_Category
class CategorySerializer(serializers. ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
class HoppiesSerializer(serializers. ModelSerializer):
    class Meta:
        model=Activity
        fields='__all__'
class BookSerializer(serializers. ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
class VideoSerializer(serializers. ModelSerializer):
    class Meta:
        model=Video
        fields='__all__'
class app_QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=app_Question
        fields='__all__'
class data_of_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Data_of_Category
        fields='__all__'
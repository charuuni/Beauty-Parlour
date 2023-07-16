from rest_framework import serializers
from . models import *
class ArticleSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=10)
    email=serializers.EmailField()
    number=serializers.IntegerField()
    def create(self, validated_data):
        return Article.objects.create(validated_data)
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.email=validated_data.get('email',instance.email)
        instance.number=validated_data.get('number',instance.number)
        instance.save()
        return instance
# class DemoSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=10)
#     age=serializers.IntegerField()
#     def create(self,validates_data):
#         return Demo.objects.create(validated_data)

class DatatypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=['id','name','email','number']



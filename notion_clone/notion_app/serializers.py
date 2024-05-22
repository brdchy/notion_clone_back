from rest_framework import serializers
from.models import Tag, Project, Doc


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class DocSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all()) 
    file = serializers.FileField(write_only=True)
    
    class Meta:
        model = Doc
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    docs = DocSerializer(many=True, read_only=True)
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all()) 
    
    class Meta:
        model = Project
        fields = '__all__'


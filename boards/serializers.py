from rest_framework import serializers
from .models import FreePost,Comment


class FreePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreePost
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.name')
    class Meta:
        model = Comment
        fields = '__all__'
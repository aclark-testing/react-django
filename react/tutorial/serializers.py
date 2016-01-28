from .models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, obj, validated_data):
        obj.text = validated_data.get('text', obj.text)
        obj.author = validated_data.get('author', obj.author)
        obj.save()
        return obj

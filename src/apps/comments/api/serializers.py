from rest_framework import serializers
from apps.comments import models
from apps.accounts.api.serializers import UserUsernameSerializer


class CommentListAllSerializer(serializers.ModelSerializer):
    user = UserUsernameSerializer()

    class Meta:
        model = models.Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = [
            'id',
            'user',
            'content_type',
            'object_id',
            'content',
        ]


class CommentRetrieveUpdateDestroySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = [
            'id',
            'user',
            'content_type',
            'object_id',
            'content',
        ]

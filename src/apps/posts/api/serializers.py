from rest_framework import serializers
from apps.accounts.api.serializers import UserUsernameSerializer
from apps.comments.api.serializers import CommentListAllSerializer

from apps.posts import models


class PostListAllSerializer(serializers.ModelSerializer):
    user = UserUsernameSerializer()
    comments = CommentListAllSerializer(many=True)

    class Meta:
        model = models.Post
        fields = [
            'id',
            'user',
            'title',
            'content',
            'file',
            'comments',
            'timestamp',
            'updated',
        ]


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = [
            'id',
            'user',
            'title',
            'content',
            'file',
        ]


class PostRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    user = UserUsernameSerializer()

    class Meta:
        model = models.Post
        fields = [
            'id',
            'user',
            'title',
            'content',
            'file',
            'updated',
        ]

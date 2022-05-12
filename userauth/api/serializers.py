from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from userauth import models


class ProfileUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProfileUser
        fields = '__all__'


class FollowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Follower
        fields = '__all__'


class PublicationListSerializer(serializers.ModelSerializer):

    user = ProfileUserSerializer(read_only=True)
    category = SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = models.Publication
        fields = '__all__'




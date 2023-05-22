from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from users import models


class ReadProfileSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(many=True, slug_field='title', read_only=True)
    specialization = serializers.SlugRelatedField(many=False, slug_field='title', read_only=True)

    class Meta:
        model = models.Profile
        exclude = ('id', 'user', 'created',)


class CreateAndUpdateProfileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        model = models.Profile
        exclude = ('created',)


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = '__all__'


class TechnologieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Technologie
        fields = '__all__'

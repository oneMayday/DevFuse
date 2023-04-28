from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from users import models


class ProfileSerializer(serializers.ModelSerializer):
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

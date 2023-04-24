from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from users.models import Profile, Technologie, Specialization


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Profile
        fields = '__all__'


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'


class TechnologieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technologie
        fields = ('id', 'title',)

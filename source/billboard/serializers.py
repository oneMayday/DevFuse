from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from users.models import Technologie, Specialization, Profile
from .models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    technology_stack = serializers.SlugRelatedField(many=True, slug_field='title', queryset=Technologie.objects.all())
    who_needs = serializers.SlugRelatedField(many=True, slug_field='title', queryset=Specialization.objects.all())
    owner = serializers.HiddenField(default=CurrentUserDefault())
    team = serializers.SlugRelatedField(
        many=True,
        slug_field='username',
        queryset=User.objects.select_related('profile').filter(profile__ready_to_work=True).all()
    )

    class Meta:
        model = Publication
        fields = ('pk', 'title', 'description', 'technology_stack', 'who_needs', 'owner', 'team')

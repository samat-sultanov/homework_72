from rest_framework import serializers
from webapp.models import Phrase


class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = ['id', 'text', 'author', 'email', 'rating', 'status', 'created_at']
        read_only_fields = ['id', 'rating', 'status', 'created_at']


class PhraseSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = ['id', 'text', 'status']

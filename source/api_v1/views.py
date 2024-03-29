from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, HttpResponseNotAllowed

from webapp.models import Phrase
from api_v1.serializers import PhraseSerializer, PhraseSerializerUpdate


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class CustomPermission(BasePermission):
    message = "You do not have permission for this action!"

    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        elif request.method == "GET":
            return True
        elif request.method == "PATCH" and request.user.has_perm('webapp.change_phrase'):
            return True
        elif request.method == "DELETE" and request.user.has_perm('webapp.delete_phrase'):
            return True
        return False


class PhraseView(APIView):
    permission_classes = [CustomPermission]

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk') and request.user.has_perm('webapp.view_new_phrases'):
            phrase = get_object_or_404(Phrase, pk=kwargs.get('pk'))
            serializer = PhraseSerializer(phrase)
        elif kwargs.get('pk') and not request.user.has_perm('webapp.view_new_phrases'):
            phrase = get_object_or_404(Phrase, pk=kwargs.get('pk'))
            if phrase.status == 'moderated':
                serializer = PhraseSerializer(phrase)
            else:
                return Response({"message": "You do not have permission for this action!"}, status=400)
        elif request.user.has_perm('webapp.view_new_phrases'):
            phrases = Phrase.objects.all()
            serializer = PhraseSerializer(phrases, many=True)
        else:
            phrases = Phrase.objects.filter(status__exact='moderated')
            serializer = PhraseSerializer(phrases, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PhraseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def get_success_url(self):
        return reverse('webapp:index')

    def patch(self, request, *args, **kwargs):
        phrase = get_object_or_404(Phrase, pk=kwargs.get('pk'))
        serializer = PhraseSerializerUpdate(data=request.data, instance=phrase)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        get_object_or_404(Phrase, pk=kwargs.get('pk')).delete()
        return Response({'deleted_phrase_pk': kwargs.get('pk')})

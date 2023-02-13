from django.urls import path
from api_v1.views import PhraseView,get_token_view

app_name = 'api_v1'


urlpatterns = [
    path('phrase/', PhraseView.as_view(), name='phrase_list'),
    path('phrase/<int:pk>/', PhraseView.as_view(), name='phrase'),
    path('get_token/', get_token_view),
]

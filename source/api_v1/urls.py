from django.urls import path, include
from api_v1.views import PhraseView
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api_v1'

phrase_url = [
    path('', PhraseView.as_view()),
    path('<int:pk>/', PhraseView.as_view()),
]

urlpatterns = [
    path('phrase/', include(phrase_url)),
    path('login/', obtain_auth_token, name='api_token_auth'),
]

from django.urls import path
from api_v1.views import PhraseView

app_name = 'api_v1'


urlpatterns = [
    path('', PhraseView.as_view(), name='phrase_list'),
    path('<int:pk>/', PhraseView.as_view(), name='phrase'),
]

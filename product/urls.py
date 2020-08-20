from django.urls import path
from .views import envelopes, giftTags, wineBags


urlpatterns = [
    path('envelopes/', envelopes, name='envelopes'),
    path('gift-tags/', giftTags, name='giftTags'),
    path('wine-bags/', wineBags, name='wineBags')
]

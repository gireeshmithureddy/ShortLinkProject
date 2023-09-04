from django.urls import path
from .views import ShortLinkCreateView, ShortLinkURLView


urlpatterns = [
    path('shortlinks/', ShortLinkCreateView.as_view(), name='shortlink-create'),
    path('shortlinks/<str:short_code>/', ShortLinkURLView.as_view(), name='shortlink-view'),
]
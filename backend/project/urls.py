from django.conf.urls import url
from .views import get_all_complaints

urlpatterns = [
    url(r'^complaints/$',get_all_complaints)
]

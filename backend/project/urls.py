from django.conf.urls import url
from .views import get_all_complaints, register_complain

urlpatterns = [
    url(r'^complaints/$',get_all_complaints),
    url(r'^register_complain/$',register_complain)
]

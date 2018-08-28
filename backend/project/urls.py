from django.conf.urls import url
from .views import get_all_complaints, register_complain, get_results, getSatAnal

urlpatterns = [
    url(r'^complaints/$',get_all_complaints),
    url(r'^register_complain/$',register_complain),
    url(r'^get_results/$',get_results),
    url(r'^satellite/$',getSatAnal),
]

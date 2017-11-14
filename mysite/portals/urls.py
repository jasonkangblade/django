
from django.conf.urls import url
from portals.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
]
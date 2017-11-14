
from django.conf.urls import url
from portals import views

urlpatterns = [
    url(r'^$',views.homepage,name='homepage'),
]
from django.conf.urls import url
from oauth2.views.authorize import AuthorizeViewDispatcher
from oauth2.views.token import TokenViewDispatcher

urlpatterns = [
    url(r'^authorize/$', AuthorizeViewDispatcher.as_view(), name='authorize'),
    url(r'^token/$', TokenViewDispatcher.as_view(), name='token'),
]

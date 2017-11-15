from django.conf.urls import url
from . import views
from .views import Add_upload,composeview,Home,logout,Delete_mail
from django.conf import settings
urlpatterns = [
    url(r'person/$',views.persondetail),
    url(r'inbox/$',views.inbox),

    url(r'home/$',views.Home.as_view()),
    url(r'compose/$',composeview.as_view()),
    url(r'add/$',Add_upload.as_view()),
    url(r'delete/(?P<pk>[0-9]+)/$', Delete_mail.as_view()),
]
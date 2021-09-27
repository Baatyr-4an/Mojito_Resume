from apps.resume import urls
from django.conf.urls import url
from django.urls import path, include
from apps.users.views import signup, login_user, profile
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    url(r'signup/$', views.signup, name="signup"),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^login/$', views.login_user, name='login'),
    url('profile/<int:id>', profile, name='profile'),
]
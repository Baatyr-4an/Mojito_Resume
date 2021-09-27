from os import name
from django.urls import path
from . import views
from apps.resume.views import index
from apps.users.views import signup, login_user
from django.contrib.auth.views import LogoutView
from .views import users_pdf_view



urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_resume, name='create'),
    path('watch_resume/', views.watch_resume, name='watch'),
    path('login/', login_user, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('pdf/<pk>/', users_pdf_view, name='users_pdf_view'),
    path('showinfo/', views.show_resume, name='show_resume'),
    path('create-pdf/', views.pdf_report_create, name='create-pdf'),
]



from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

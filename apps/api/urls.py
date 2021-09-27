from django.urls import path 

from .api_views import ResumeListAPIView


urlpatterns = [
    path('categories/', ResumeListAPIView.as_view(), name='resumes')
]


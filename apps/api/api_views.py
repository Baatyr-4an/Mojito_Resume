from rest_framework import serializers
from rest_framework.generics import ListAPIView

from .serializer import ResumeSerializer
from apps.resume.models import Resume

class ResumeListAPIView(ListAPIView):

    serializer_class = ResumeSerializer
    queriset = Resume.objects.all()
    
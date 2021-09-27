from rest_framework import serializers

from apps.resume.models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    
    # name = serializers.CharField(read_only=True)
    # surname = serializers.CharField(read_only=True)
    # midlename = serializers.CharField(read_only=True)
    # citizenship = serializers.CharField(read_only=True)
    # nationality = serializers.CharField(read_only=True)
    # wish_post = serializers.CharField(read_only=True)
    # about_yourself = serializers.CharField(read_only=True)
    # accounts = serializers.URLField(read_only=True)
    # burn_date = serializers.DateField(read_only=True)
    # contacts = serializers.IntegerField(read_only=True)
    # email = serializers.EmailField(only_read=True)

    class Meta:
        model = Resume
        fields = '__all__'
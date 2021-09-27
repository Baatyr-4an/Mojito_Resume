from django import forms
from django.forms.widgets import TextInput
from .models import Resume, ResumeImage

class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = [ 
            'name', 
            'surname', 
            'midlename', 
            'citizenship', 
            'nationality', 
            'wish_post', 
            'about_yourself', 
            'accounts', 
            'contacts', 
            'email',
            ]
            
        
class ResumeImageForm(forms.ModelForm):
    class Meta:
        model = ResumeImage
        fields = ['image', ]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
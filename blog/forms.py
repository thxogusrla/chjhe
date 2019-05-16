from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'card border-left-primary shadow h-100  py-2', 'placeholder': '제목.'}),
            'body': forms.TextInput(attrs={'class': 'card border-left-primary shadow h-100 py-2', 'placeholder': '내용.'}),
        }
        
        labels = {
            'title' : '   제목   ',
            'body' : '   내용   ',        
            }
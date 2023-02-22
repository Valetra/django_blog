from django import forms
from .models import Post, Category

category_choices = Category.objects.all().values_list('name', 'name')

class PostForm(forms.ModelForm):
    class Meta:   
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'author', 'type': 'hidden'}),
            'category': forms.Select(choices=category_choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Here you can place a snippet of your article that will be displayed on the home page'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=category_choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }
  
class AddCategoryForm(forms.ModelForm):
    class Meta:   
        model = Category
        fields = ('name',)
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

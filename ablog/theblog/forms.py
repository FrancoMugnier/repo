'''
from django import forms
from .models import post, category, Comment

choices=category.objects.all().values_list('name','name')

choice_list=[]

for item in choices:
    choice_list.append(item)

class formpost(forms.ModelForm):
    class Meta:
        model=post
        fields=['title', 'author', 'category' , 'body', 'snippet','header_image']

        widgets= {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'frank', 'type':'hidden'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list ,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

class editpost(forms.ModelForm):
    class Meta:
        model=post
        fields=['title', 'author', 'body', 'snippet']

        widgets= {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name', 'body']

        widgets= {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            #'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

'''

from django import forms
from .models import post, category, Comment

choices = category.objects.all().values_list('name', 'name')

choice_list = []
for item in choices:
    choice_list.append(item)

class formpost(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title', 'author', 'category', 'body', 'snippet', 'header_image']
        labels = {
            'title': 'Título',
            'author': 'Autor',
            'category': 'Categoría',
            'body': 'Contenido',
            'snippet': 'Resumen',
            'header_image': 'Imagen de Encabezado',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

class editpost(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title', 'author', 'body', 'snippet']
        labels = {
            'title': 'Título',
            'author': 'Autor',
            'body': 'Contenido',
            'snippet': 'Resumen',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        labels = {
            'name': 'Nombre',
            'body': 'Comentario',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

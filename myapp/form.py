from django import forms
from .models import Todo, Blog


class MyTodo(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['task']

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['title','body']

from django.forms import ModelForm, Textarea
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('author',)
        widget = {
            'body': Textarea(attrs={'cols': 10, 'rows': 10})
        }

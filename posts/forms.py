from django import forms
from .models import Post

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        #fields which user can actually edit hence no views or created_date
        fields = ('title', 'content', 'image', 'tag', 'published_date') 
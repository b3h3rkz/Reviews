from django.forms import ModelForm
from .models import Comments


class CommentsModelForm(ModelForm):
    model = Comments
    fields =  ('comment',)
    exclude = ['post']

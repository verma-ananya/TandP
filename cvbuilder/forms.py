from django.forms import ModelForm
from cvbuilder.models import CV_attr


class myModelForm(ModelForm):
    class Meta:
        model = CV_attr
        fields = '__all__'

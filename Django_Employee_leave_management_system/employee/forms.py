from django.forms import ModelForm
from .models import leave_request


class leaving_apply(ModelForm):
    class Meta:
        model = leave_request
        fields = ['Subject', 'Reason']

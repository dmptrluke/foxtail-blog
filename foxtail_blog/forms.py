from captcha.fields import ReCaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.conf import settings
from django.forms import ModelForm, Textarea

from .models import Comment


class CommentForm(ModelForm):
    if settings.RECAPTCHA_ENABLED:
        captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

        self.helper.layout = Layout(
            'text',
            'captcha',
            Submit('submit', 'Post Comment')
        )

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'rows': 4})
        }

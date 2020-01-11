from django.forms import ModelForm, Textarea

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from csp_helpers.mixins import CSPFormMixin

from . import settings as app_settings
from .models import Comment


class CommentForm(CSPFormMixin, ModelForm):
    if app_settings.RECAPTCHA_ENABLED:
        if app_settings.RECAPTCHA_INVISIBLE:
            captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)
        else:
            captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.error_text_inline = False
        self.helper.help_text_inline = False

        self.helper.layout = Layout(
            'text',
            'captcha' if app_settings.RECAPTCHA_ENABLED else None,
            Submit('Post Comment', 'Post Comment')
        )

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'rows': 4})
        }

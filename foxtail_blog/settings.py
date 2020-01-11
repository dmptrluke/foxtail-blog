from django.conf import settings

RECAPTCHA_ENABLED = getattr(settings, 'RECAPTCHA_ENABLED', True)
RECAPTCHA_INVISIBLE = getattr(settings, 'RECAPTCHA_INVISIBLE', False)

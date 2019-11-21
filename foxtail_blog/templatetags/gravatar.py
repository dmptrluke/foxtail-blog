from hashlib import md5
from urllib.parse import urlencode
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# return only the URL of the gravatar
# TEMPLATE USE:  {{ email|gravatar_url:150 }}
@register.filter
def gravatar_url(email, size=40):
    default = "https://example.com/static/images/defaultavatar.jpg"
    return "https://www.gravatar.com/avatar/{}?{}".format(
    md5(email.lower().encode('utf-8')).hexdigest(), urlencode({'d': default, 's': str(size)}))


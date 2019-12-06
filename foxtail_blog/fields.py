from dataclasses import dataclass
from functools import partial
from urllib.parse import urlparse

import bleach
import bleach_whitelist
from bleach.linkifier import LinkifyFilter
from django.conf import settings
from django.db.models import TextField
from markdown import markdown

from typing import List

EXTENSIONS = getattr(settings, 'MARKDOWN_EXTENSIONS', [])
EXTENSION_CONFIGS = getattr(settings, 'MARKDOWN_EXTENSION_CONFIGS', [])


@dataclass
class Validator:
    """ defines a standard format for markdown validators """
    allowed_tags: List[str]
    allowed_attrs: dict
    sanitize: bool


VALIDATOR_NULL = Validator(
    allowed_tags=[],
    allowed_attrs={},
    sanitize=False
)

VALIDATOR_STANDARD = Validator(
    allowed_tags=bleach_whitelist.markdown_tags + ['pre', 'dl', 'del', 'abbr'],
    allowed_attrs={
        **bleach_whitelist.markdown_attrs,
        'abbr': ['title']
    },
    sanitize=True
)

VALIDATOR_CLASSY = Validator(
    allowed_tags=bleach_whitelist.markdown_tags + ['pre', 'dl', 'del', 'abbr'],
    allowed_attrs={
        **bleach_whitelist.markdown_attrs,
        'abbr': ['title'],
        'img': ['src', 'alt', 'title', 'class'],
        'a': ['href', 'alt', 'title', 'name', 'class']
    },
    sanitize=True
)


def set_target(attrs, new=False):
    """
    This is kinda weird and ugly, but that's how bleach linkify filters work.
    TODO: redo this all.
    """
    try:
        p = urlparse(attrs[(None, 'href')])
    except KeyError:
        # no href, probably an anchor
        return attrs

    if not any([p.scheme, p.netloc, p.path]) and p.fragment:
        # the link isn't going anywhere, probably a fragment link
        attrs.pop((None, 'target'), None)
        return attrs

    c = urlparse(settings.SITE_URL)
    if p.netloc != c.netloc:
        attrs[(None, 'target')] = '_blank'
        attrs[(None, 'class')] = attrs.get((None, 'class'), '') + ' external'
        attrs[(None, 'rel')] = 'nofollow noopener noreferrer'
    else:
        attrs.pop((None, 'target'), None)
    return attrs


class RenderedMarkdownField(TextField):
    def __init__(self, *args, **kwargs):
        kwargs['editable'] = False
        kwargs['blank'] = False
        super().__init__(*args, **kwargs)


class MarkdownField(TextField):
    def __init__(self, *args, rendered_field=None, validator=VALIDATOR_STANDARD, **kwargs):
        self.rendered_field = rendered_field
        self.validator = validator
        kwargs['help_text'] = 'This field supports <a href="https://commonmark.org/help/" target="_blank"' \
                              '>Markdown</a> formatting.'
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = super(MarkdownField, self).pre_save(model_instance, add)

        if not self.rendered_field:
            return value

        dirty = markdown(
            text=value,
            extensions=EXTENSIONS,
            extension_configs=EXTENSION_CONFIGS
        )

        if self.validator.sanitize:
            cleaner = bleach.Cleaner(tags=self.validator.allowed_tags,
                                     attributes=self.validator.allowed_attrs,
                                     filters=[partial(LinkifyFilter, callbacks=[set_target])])
            clean = cleaner.clean(dirty)
            setattr(model_instance, self.rendered_field, clean)
        else:
            # danger!
            setattr(model_instance, self.rendered_field, dirty)

        return value

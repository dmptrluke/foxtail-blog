from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'foxtail_blog'
    verbose_name = 'Foxtail Blog'

    def ready(self):
        # import signal handlers
        # noinspection PyUnresolvedReferences
        import foxtail_blog.signals

from django.apps import AppConfig
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import post_save
from django.conf import settings


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self) -> None:
        from . import signals  # noqa

        post_save.connect(signals.user_created_handler, sender=settings.AUTH_USER_MODEL)

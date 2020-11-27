from django.conf import settings

# from loguru import logger

from .models import Profile

# logger.add(
#     str(settings.BASE_DIR / 'accounts' / 'logs' / 'log_in_out.log'),
#     rotation='100MB',
#     format='{time} {message}',
# )


def user_created_handler(sender, **kwargs) -> None:
    """Создать пользовательское меню при создании пользователя."""
    if not kwargs['created']:
        # если пользователя не создавали, а меняли
        return
    user = kwargs['instance']
    user_menu = Profile(user=user)
    user_menu.save()


# def log_login(sender, user, request, **kwargs) -> None:
#     """Логгировать успешные входы на сайт."""
#     logger.info(f'{user} login')


# def log_logout(sender, user, request, **kwargs) -> None:
#     """Логгировать выходы с сайта."""
#     if user is not None:
#         logger.info(f'{user} logout')

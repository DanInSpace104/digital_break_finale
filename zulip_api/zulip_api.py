#!/usr/bin/env python3
import zulip
from django.conf import settings

# Pass the path to your zuliprc file here.
client = zulip.Client(config_file=str(settings.BASE_DIR / "zulip_api/.zuliprc"))


def zulip_create_stram(expert_mail, user_list, id_in_db_case, name_case, category):
    '''
    На вход получаем 5 аргументов, где:
        expert_mail, является строкой и означает почту эксперта
        user_list, список объектов юзера в виде list-а
        id_in_db_case, ID кейса в БД (int)
        name_case, Имя кейса (строка)
        category, К какой категории относится кейс (строка)
    Функция создает стрим в зулипе и добавляет туда всех юзеров и эксперта
    '''
    user_mail_list = []
    for e in user_list:
        user_mail_list.append(e.email)

    result = client.call_endpoint(
        url='users?client_gravatar=true',
        method='GET',
    )

    # Находим в динамике ID нужного эксперта, кого закрепить за стримом
    admins_id = []
    for user in result['members']:
        if user['email'] == expert_mail:
            admins_id.append(user['user_id'])
        elif user['email'] in user_mail_list:
            admins_id.append(user['user_id'])

    # Создать стрим
    result = client.add_subscriptions(
        streams=[
            {
                'name': f'{id_in_db_case}: {name_case}',
                'description': f'Категория: {category}',
            },
        ],
        principals=admins_id,  # Участники стрима
    )

#!/usr/bin/env python3
import zulip

# Pass the path to your zuliprc file here.
client = zulip.Client(config_file="~/zuliprc")

# expert_mail = 'konshin104@gmail.com'
# user_mail = 'BlueSkyC@mail.ru'

# id_in_db_case = 104
# name_case = 'Вариант докреентации кеверниции'
# category = 'ДокРеентация'


def zulip_create_stram(expert_mail, user_mail, id_in_db_case, name_case, category):
    result = client.call_endpoint(
        url='users?client_gravatar=true',
        method='GET',
    )

    # Находим в динамике ID нужного эксперта, кого закрепить за стримом
    admins_id = []
    for user in result['members']:
        if (user['email'] == expert_mail) or (user['email'] == user_mail):
            expert_id = user['user_id']
            print(user['user_id'])

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

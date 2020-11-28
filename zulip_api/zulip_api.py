#!/usr/bin/env python3
import zulip
from django.conf import settings

# Pass the path to your zuliprc file here.
client = zulip.Client(config_file=str(settings.BASE_DIR / "zulip_api/.zuliprc"))

# expert_mail = 'konshin104@gmail.com'
# user_mail = 'BlueSkyC@mail.ru'

# id_in_db_case = 104
# name_case = 'Вариант докреентации кеверниции'
# category = 'ДокРеентация'


def zulip_create_stream(expert_mail, user_mail, claim_id, claim_name, category):
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
                'name': f'{claim_id}: {claim_name}',
                'description': f'Категория: {category}',
            },
        ],
        principals=admins_id,  # Участники стрима
    )

# Generated by Django 3.1.3 on 2020-11-27 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='profiles/default.png', upload_to='profiles'),
        ),
    ]

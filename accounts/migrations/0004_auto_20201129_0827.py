# Generated by Django 3.1.3 on 2020-11-29 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('racs', '0007_claim_similars'),
        ('accounts', '0003_profile_otdel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='otdel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='profiles', to='racs.otdel'),
        ),
    ]

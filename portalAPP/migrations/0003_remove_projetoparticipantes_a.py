# Generated by Django 2.2.6 on 2019-11-08 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portalAPP', '0002_projetoparticipantes_a'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projetoparticipantes',
            name='a',
        ),
    ]
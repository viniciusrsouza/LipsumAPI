# Generated by Django 2.2.6 on 2019-11-19 23:58

from django.db import migrations, models
import portalAPP.models


class Migration(migrations.Migration):

    dependencies = [
        ('portalAPP', '0011_evento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data',
            field=models.DateTimeField(validators=[portalAPP.models.Evento.validate_date]),
        ),
    ]

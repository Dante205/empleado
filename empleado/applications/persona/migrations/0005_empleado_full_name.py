# Generated by Django 3.1.5 on 2021-01-28 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_auto_20210126_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombres Completos'),
        ),
    ]

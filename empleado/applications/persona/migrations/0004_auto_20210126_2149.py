# Generated by Django 3.1.5 on 2021-01-27 02:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_auto_20210126_1959'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados de la Empresa'},
        ),
        migrations.AddField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default='texto'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.7 on 2021-02-20 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0009_remove_plataforma_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plataforma',
            old_name='funcionario',
            new_name='usuario',
        ),
    ]

# Generated by Django 3.1.7 on 2021-02-20 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0006_auto_20210219_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='plataforma',
            name='funcionario',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]

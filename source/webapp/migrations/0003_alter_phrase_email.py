# Generated by Django 4.1.6 on 2023-02-13 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_phrase_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phrase',
            name='email',
            field=models.EmailField(max_length=70, unique=True, verbose_name='Почта'),
        ),
    ]

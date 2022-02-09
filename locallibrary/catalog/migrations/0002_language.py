# Generated by Django 4.0.2 on 2022-02-08 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Entrez la langue naturelle du livre (par exemple, anglais, français, japonais, etc.)', max_length=200, verbose_name='Langue')),
            ],
        ),
    ]

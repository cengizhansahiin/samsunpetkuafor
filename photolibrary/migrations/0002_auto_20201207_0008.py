# Generated by Django 3.1.3 on 2020-12-06 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photolibrary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photolibrary',
            name='kind',
            field=models.CharField(choices=[('Poodle', 'Poodle'), ('Pomeranian', 'Pomeranian'), ('Shih Tzu', 'Shih Tzu'), ('Yorkshire Terrier', 'Yorkshire Terrier'), ('Maltese Terrier', 'Maltese Terrier'), ('Minyatür Schnauzer', 'Minyatür Schnauzer')], max_length=20),
        ),
    ]

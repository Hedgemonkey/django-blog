# Generated by Django 5.1.2 on 2024-10-27 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_alter_about_updated_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['-updated_on']},
        ),
        migrations.RemoveField(
            model_name='about',
            name='created_on',
        ),
    ]
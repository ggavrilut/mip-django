# Generated by Django 2.2.6 on 2019-11-14 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogEntry',
            new_name='Entry',
        ),
        migrations.RenameModel(
            old_name='BlogTag',
            new_name='Tag',
        ),
    ]

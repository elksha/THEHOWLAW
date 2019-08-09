# Generated by Django 2.2.3 on 2019-08-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('howlaw', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='img',
        ),
        migrations.RemoveField(
            model_name='post',
            name='price',
        ),
        migrations.RemoveField(
            model_name='post',
            name='score',
        ),
        migrations.AddField(
            model_name='post',
            name='pwd',
            field=models.CharField(default=12, max_length=200),
            preserve_default=False,
        ),
    ]

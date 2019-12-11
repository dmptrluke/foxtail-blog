# Generated by Django 2.2.7 on 2019-11-18 05:25

from django.db import migrations, models

from markdownfield.fields import MarkdownField


class Migration(migrations.Migration):

    dependencies = [
        ('foxtail_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text_rendered',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=MarkdownField(),
        ),
    ]

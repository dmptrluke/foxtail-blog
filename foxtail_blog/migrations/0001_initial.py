# Generated by Django 2.2.7 on 2019-11-15 02:08

from django.db import migrations, models

import taggit.managers
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='100 characters or fewer.', max_length=100)),
                ('slug', models.SlugField(help_text='Changing this value after initial creation will break existing post URLs. Must be unique.', unique=True)),
                ('author', models.CharField(help_text='50 characters or fewer.', max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='blog')),
                ('image_ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
                ('text', models.TextField()),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]

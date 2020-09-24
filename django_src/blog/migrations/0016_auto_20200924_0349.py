# Generated by Django 3.1 on 2020-09-23 18:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200924_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='article_likes',
            field=models.ManyToManyField(blank=True, db_constraint=False, null=True, related_name='article_user_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]

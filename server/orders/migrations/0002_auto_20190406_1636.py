# Generated by Django 2.2 on 2019-04-06 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='hash_signature',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='filled',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='size',
            field=models.IntegerField(default=0),
        ),
    ]
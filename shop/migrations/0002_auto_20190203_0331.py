# Generated by Django 2.1.5 on 2019-02-03 03:31

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to=''),
        ),
    ]

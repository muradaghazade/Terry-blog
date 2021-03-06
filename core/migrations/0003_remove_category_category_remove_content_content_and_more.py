# Generated by Django 4.0.2 on 2022-02-09 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_content_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category',
        ),
        migrations.RemoveField(
            model_name='content',
            name='content',
        ),
        migrations.AddField(
            model_name='posts',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='core.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='content',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='core.content'),
            preserve_default=False,
        ),
    ]

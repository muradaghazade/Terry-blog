# Generated by Django 4.0.2 on 2022-02-09 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='content',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='core.posts'),
            preserve_default=False,
        ),
    ]
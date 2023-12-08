# Generated by Django 4.2.7 on 2023-11-30 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='period',
            field=models.ForeignKey(default=2023, on_delete=django.db.models.deletion.PROTECT, to='app.period'),
            preserve_default=False,
        ),
    ]

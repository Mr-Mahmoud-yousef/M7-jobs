# Generated by Django 3.1.2 on 2020-10-05 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_referanse'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='referanse',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='job.referanse'),
            preserve_default=False,
        ),
    ]
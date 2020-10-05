# Generated by Django 3.1.2 on 2020-10-05 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20201005_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='Discription',
        ),
        migrations.RemoveField(
            model_name='job',
            name='Experience',
        ),
        migrations.RemoveField(
            model_name='job',
            name='Job_Type',
        ),
        migrations.RemoveField(
            model_name='job',
            name='salery',
        ),
        migrations.AddField(
            model_name='job',
            name='DiscRIPION',
            field=models.TextField(default='', max_length=600),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='ExperIENCE',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='Job_TYPE',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='salERY',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='vacAnCY',
            field=models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five'), (6, 'Sex'), (7, 'Seven')], default=0),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-22 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20210322_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='static/projects/images'),
        ),
    ]

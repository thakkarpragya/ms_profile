# Generated by Django 3.2.15 on 2022-09-08 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profileuser', '0003_auto_20220908_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='regID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profileuser.profile'),
        ),
    ]

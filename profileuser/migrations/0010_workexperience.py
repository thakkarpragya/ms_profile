# Generated by Django 3.2.15 on 2022-09-09 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profileuser', '0009_delete_workexperience'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('startYear', models.DateField()),
                ('endYear', models.DateField()),
                ('designation', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('regId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profileuser.profile')),
            ],
        ),
    ]

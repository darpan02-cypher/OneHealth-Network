# Generated by Django 2.2.6 on 2019-10-22 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientmedicalhistory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedHistoryInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom', models.CharField(default='symptoms', max_length=100)),
            ],
        ),
    ]

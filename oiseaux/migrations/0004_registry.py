# Generated by Django 5.1 on 2024-08-11 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oiseaux', '0003_sample_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registry_title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=13)),
                ('event_date', models.DateField()),
                ('message', models.CharField(max_length=256)),
                ('registry_link', models.CharField(max_length=50)),
                ('show_who_sent_gifts', models.BooleanField(default=True)),
                ('dark_mode', models.BooleanField(default=False)),
                ('photo', models.CharField(max_length=250)),
                ('ocassion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registries', to='oiseaux.ocassion')),
            ],
        ),
    ]

# Generated by Django 5.1 on 2024-08-11 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oiseaux', '0005_remove_registry_name_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('art_id', models.IntegerField()),
                ('note', models.CharField(max_length=256)),
                ('accepted', models.BooleanField(default=False)),
                ('registry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gifts', to='oiseaux.registry')),
            ],
        ),
    ]

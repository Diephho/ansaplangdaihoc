# Generated by Django 5.0.3 on 2024-05-06 04:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0016_post_numcreact_post_totalstar'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryChat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=1000)),
                ('fromAI', models.BooleanField(default=0)),
                ('iduser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DjangoApp.userinfo')),
            ],
        ),
    ]

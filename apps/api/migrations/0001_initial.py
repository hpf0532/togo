# Generated by Django 3.0.6 on 2020-07-01 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rsa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(1, '启用'), (2, '停用')], verbose_name='状态')),
                ('user', models.CharField(default='root', max_length=32, verbose_name='用户')),
                ('private_key', models.TextField(verbose_name='私钥')),
            ],
        ),
    ]
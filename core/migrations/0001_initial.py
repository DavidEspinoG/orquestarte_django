# Generated by Django 4.1.4 on 2022-12-08 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClaseVirtual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
            options={
                'verbose_name': 'clase virtual',
                'verbose_name_plural': 'clases virtuales',
            },
        ),
    ]
# Generated by Django 3.1.1 on 2021-06-15 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_image', models.ImageField(upload_to='item_images/')),
                ('item_text', models.CharField(max_length=300)),
            ],
        ),
    ]

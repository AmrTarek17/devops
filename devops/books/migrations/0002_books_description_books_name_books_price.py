# Generated by Django 4.1.4 on 2022-12-14 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='books',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='books',
            name='price',
            field=models.IntegerField(default=100),
        ),
    ]
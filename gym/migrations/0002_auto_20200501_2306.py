# Generated by Django 3.0.3 on 2020-05-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipment',
            old_name='date',
            new_name='date1',
        ),
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
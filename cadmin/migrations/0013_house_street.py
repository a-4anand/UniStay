# Generated by Django 4.2.5 on 2024-01-25 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadmin', '0012_rename_street_imaage_streets_street_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='street',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cadmin.streets'),
        ),
    ]
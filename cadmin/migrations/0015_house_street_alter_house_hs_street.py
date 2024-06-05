# Generated by Django 4.2.5 on 2024-01-25 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadmin', '0014_remove_house_street_alter_house_hs_street'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='street',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cadmin.streets'),
        ),
        migrations.AlterField(
            model_name='house',
            name='hs_street',
            field=models.CharField(default='Not specified', max_length=50),
        ),
    ]
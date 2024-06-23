# Generated by Django 5.0.6 on 2024-06-23 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_patient_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medication',
            name='remarks',
        ),
        migrations.AlterField(
            model_name='consult',
            name='visit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.visit'),
        ),
        migrations.AlterField(
            model_name='order',
            name='consult',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prescriptions', to='api.consult'),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='blood_glucose',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='diastolic',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='heart_rate',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='hemocue_count',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='systolic',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='temperature',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]

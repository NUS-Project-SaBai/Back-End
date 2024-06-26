# Generated by Django 4.2 on 2024-02-15 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("clinicmodels", "0016_alter_patient_picture"),
    ]

    operations = [
        migrations.CreateModel(
            name="Diagnosis",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("details", models.TextField(blank=True, null=True)),
                ("category", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "db_table": "diagnosis",
            },
        ),
        migrations.RenameField(
            model_name="consult",
            old_name="diagnosis",
            new_name="consultation",
        ),
        migrations.RenameField(
            model_name="consult",
            old_name="problems",
            new_name="past_medical_history",
        ),
        migrations.RemoveField(
            model_name="consult",
            name="addendum",
        ),
        migrations.RemoveField(
            model_name="consult",
            name="addendum_doctor",
        ),
        migrations.RemoveField(
            model_name="consult",
            name="addendum_time",
        ),
        migrations.RemoveField(
            model_name="consult",
            name="chronic_referral",
        ),
        migrations.RemoveField(
            model_name="consult",
            name="notes",
        ),
        migrations.RemoveField(
            model_name="consult",
            name="referrals",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="local_name",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="parent",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="travelling_time_to_village",
        ),
        migrations.RemoveField(
            model_name="vitals",
            name="cataracts",
        ),
        migrations.RemoveField(
            model_name="vitals",
            name="eye_pressure",
        ),
        migrations.RemoveField(
            model_name="vitals",
            name="hepc_positive",
        ),
        migrations.RemoveField(
            model_name="vitals",
            name="hiv_positive",
        ),
        migrations.RemoveField(
            model_name="vitals",
            name="ptb_positive",
        ),
        migrations.AddField(
            model_name="consult",
            name="plan",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="consult",
            name="referral_notes",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="consult",
            name="referred_for",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="consult",
            name="remarks",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="patient",
            name="identification_number",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="consult",
            name="visit",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="clinicmodels.visit",
            ),
        ),
        migrations.AlterField(
            model_name="vitals",
            name="visit",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="clinicmodels.visit",
            ),
        ),
        migrations.DeleteModel(
            name="Fingerprint",
        ),
        migrations.AddField(
            model_name="diagnosis",
            name="consult",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="clinicmodels.consult",
            ),
        ),
    ]

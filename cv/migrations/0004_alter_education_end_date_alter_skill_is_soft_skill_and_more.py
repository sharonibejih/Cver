# Generated by Django 4.1 on 2022-08-26 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_rename_job_title_workhistory_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='is_soft_skill',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='workhistory',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.1 on 2022-08-28 08:36

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_alter_education_end_date_alter_skill_is_soft_skill_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='currently_attend_here',
            new_name='currently_attending_here',
        ),
        migrations.RenameField(
            model_name='education',
            old_name='field_of_study',
            new_name='school_location_city',
        ),
        migrations.RemoveField(
            model_name='education',
            name='school_location',
        ),
        migrations.AddField(
            model_name='education',
            name='description',
            field=models.TextField(default=False),
        ),
        migrations.AddField(
            model_name='education',
            name='school_location_country',
            field=django_countries.fields.CountryField(default=False, max_length=2),
        ),
    ]

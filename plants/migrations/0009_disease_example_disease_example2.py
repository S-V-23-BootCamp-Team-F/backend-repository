# Generated by Django 4.1.5 on 2023-01-26 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0008_rename_plant_type_plant_type_alter_diagnosis_disease_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='example',
            field=models.URLField(default='', verbose_name='질병사진예시'),
        ),
        migrations.AddField(
            model_name='disease',
            name='example2',
            field=models.URLField(default='', verbose_name='질병사진예시2'),
        ),
    ]

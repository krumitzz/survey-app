# Generated by Django 3.2.5 on 2021-08-22 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0003_rename_owner_userdetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='department_discipline',
            field=models.CharField(blank=True, max_length=250, verbose_name='Department/Discipline'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='Date Of Birth'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('R', 'Rather Not Say')], default=('R', 'Rather Not Say'), max_length=1),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='school_or_inst',
            field=models.CharField(blank=True, max_length=250, verbose_name='School or Institution'),
        ),
    ]
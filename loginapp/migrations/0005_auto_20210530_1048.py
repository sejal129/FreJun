# Generated by Django 3.2.3 on 2021-05-30 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0004_rename_conatctnumber_userdetails_contactnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidateName', models.CharField(max_length=50)),
                ('phoneNumber', models.IntegerField()),
                ('documentName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentName', models.FileField(upload_to='')),
                ('uploadDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='LoginDetails',
            new_name='Login_Details',
        ),
        migrations.RenameModel(
            old_name='UserDetails',
            new_name='User_Details',
        ),
    ]

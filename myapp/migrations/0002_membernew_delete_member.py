# Generated by Django 5.0 on 2024-01-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membernew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('rollno', models.IntegerField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
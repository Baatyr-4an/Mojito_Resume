# Generated by Django 2.2.12 on 2021-09-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='profiles')),
                ('bio', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField(default=0)),
                ('gender', models.CharField(choices=[('m', 'Men'), ('f', 'Female'), ("I don't know", 'Trans')], max_length=255)),
            ],
        ),
    ]
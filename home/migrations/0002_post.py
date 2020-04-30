# Generated by Django 3.0.5 on 2020-04-14 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=13)),
                ('slug', models.CharField(max_length=130)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]

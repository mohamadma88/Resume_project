# Generated by Django 4.2.6 on 2024-12-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introducing', models.TextField()),
                ('name', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('workexp', models.TextField()),
                ('namecompany', models.CharField(blank=True, max_length=200, null=True)),
                ('work', models.CharField(blank=True, max_length=200, null=True)),
                ('textaward', models.TextField()),
                ('skill', models.ManyToManyField(related_name='item', to='home_app.skill')),
            ],
        ),
    ]

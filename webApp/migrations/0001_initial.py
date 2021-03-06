# Generated by Django 2.1.3 on 2018-11-25 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_candidates', models.IntegerField()),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('subject', models.TextField()),
                ('message', models.TextField()),
                ('postulation_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_member', models.IntegerField()),
                ('nickname', models.TextField(unique=True)),
                ('password', models.TextField()),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_project', models.IntegerField()),
                ('name', models.TextField(unique=True)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_semester', models.IntegerField()),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='project_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webApp.Project'),
        ),
    ]

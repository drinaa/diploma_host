# Generated by Django 3.1.7 on 2021-03-31 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('point', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='professions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='reg_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=20)),
                ('mid_name', models.CharField(max_length=30)),
                ('passport', models.CharField(max_length=10)),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='diploma_app.professions')),
                ('reg_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='diploma_app.reg_user')),
            ],
        ),
        migrations.CreateModel(
            name='pupil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=20)),
                ('doc_num', models.CharField(max_length=12)),
                ('date_of_birth', models.DateField()),
                ('grade', models.IntegerField()),
                ('letter_grade', models.CharField(max_length=1)),
                ('reg_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='diploma_app.reg_user')),
            ],
        ),
        migrations.CreateModel(
            name='diplomas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('year', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('nomination', models.CharField(max_length=25)),
                ('type', models.IntegerField()),
                ('level', models.IntegerField()),
                ('place', models.IntegerField()),
                ('part1', models.IntegerField()),
                ('part2', models.IntegerField()),
                ('point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diploma_app.points')),
                ('pupil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diploma_app.pupil')),
            ],
        ),
    ]

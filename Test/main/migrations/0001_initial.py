# Generated by Django 4.2.2 on 2023-06-17 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_scores', models.IntegerField(verbose_name='Баллы за тест')),
                ('emotionalnay_osvedomlennost', models.IntegerField(verbose_name='Эмоциональная осведомленность')),
                ('ypravlenie_svoimi_emotiymi', models.IntegerField(verbose_name='Управление своими эмоциями')),
                ('samomotivatiy', models.IntegerField(verbose_name='Самомотивация')),
                ('empatiy', models.IntegerField(verbose_name='Эмпатия')),
                ('raspoznanie_emotiy_drugih_lydey', models.IntegerField(verbose_name='Распознание эмоций других людей')),
                ('students', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.students')),
            ],
        ),
        migrations.CreateModel(
            name='Filvord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_filvord', models.IntegerField(verbose_name='Баллы за филворд')),
                ('students', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.students')),
            ],
        ),
    ]

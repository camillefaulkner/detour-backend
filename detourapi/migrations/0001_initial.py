# Generated by Django 4.0.6 on 2022-08-05 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DetourUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('allergies', models.CharField(max_length=40)),
                ('greenroom_requests', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicURL', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detourapi.detouruser')),
            ],
        ),
        migrations.CreateModel(
            name='DocAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detourapi.doc')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ShowDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('venue', models.CharField(max_length=30)),
                ('street_address', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=10)),
                ('essential_notes', models.CharField(max_length=100)),
                ('other', models.CharField(max_length=100)),
                ('docs', models.ManyToManyField(related_name='showdates_by_doc', through='detourapi.DocAssignment', to='detourapi.doc')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detourapi.detouruser')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('description', models.CharField(max_length=40)),
                ('show_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_items', to='detourapi.showdate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detourapi.detouruser')),
            ],
        ),
        migrations.CreateModel(
            name='GuestRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('quantity', models.IntegerField()),
                ('show_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guest_requests', to='detourapi.showdate')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guest_requests', to='detourapi.status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detourapi.detouruser')),
            ],
        ),
        migrations.CreateModel(
            name='GreenRoomRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.CharField(max_length=40)),
                ('show_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gr_requests', to='detourapi.showdate')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gr_requests', to='detourapi.status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detourapi.detouruser')),
            ],
        ),
        migrations.AddField(
            model_name='docassignment',
            name='show_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detourapi.showdate'),
        ),
    ]

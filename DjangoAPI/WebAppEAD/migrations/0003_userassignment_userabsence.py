# Generated by Django 4.0.3 on 2022-05-30 14:43

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('WebAppEAD', '0002_rename_materialid_material_materialid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAssignment',
            fields=[
                ('assignmentId', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('identifier', models.IntegerField()),
                ('studentId', models.IntegerField()),
                ('title', models.CharField(max_length=1500)),
                ('classId', models.IntegerField()),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
                ('createdBy', models.IntegerField()),
                ('updatedBy', models.IntegerField()),
                ('deliveredAt', models.DateTimeField()),
                ('deliveredMaterial', models.CharField(max_length=1500)),
                ('score', models.FloatField()),
                ('attachment', models.CharField(max_length=1500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebAppEAD.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserAbsence',
            fields=[
                ('absenceId', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('count', models.IntegerField()),
                ('classId', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebAppEAD.user')),
            ],
        ),
    ]
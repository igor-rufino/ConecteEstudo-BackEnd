# Generated by Django 4.0.3 on 2022-07-01 22:05

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('absenceId', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('studentId', models.IntegerField()),
                ('count', models.IntegerField()),
                ('classId', models.IntegerField()),
                ('date', models.DateField()),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
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
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('classroomId', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
                ('createdBy', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eventId', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('eventType', models.IntegerField()),
                ('classId', models.IntegerField()),
                ('teacherName', models.CharField(max_length=1500)),
                ('title', models.CharField(max_length=1500)),
                ('description', models.CharField(max_length=1500)),
                ('dateOfEvent', models.DateTimeField()),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
                ('updatedBy', models.IntegerField()),
                ('status', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('MaterialId', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1500)),
                ('description', models.CharField(max_length=1500)),
                ('attachment', models.CharField(max_length=1500)),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
                ('createdBy', models.IntegerField()),
                ('classId', models.IntegerField()),
                ('teacherId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TeachingPlan',
            fields=[
                ('teachingPlanId', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('classId', models.IntegerField()),
                ('title', models.CharField(max_length=1500)),
                ('state', models.IntegerField()),
                ('workload', models.IntegerField()),
                ('absencesLimit', models.IntegerField()),
                ('year', models.CharField(max_length=1500)),
                ('teacherName', models.CharField(max_length=1500)),
                ('content', models.CharField(max_length=1500)),
                ('objective', models.CharField(max_length=1500)),
                ('teachingProcedure', models.CharField(max_length=1500)),
                ('didacticResource', models.CharField(max_length=1500)),
                ('evaluationProcedure', models.CharField(max_length=1500)),
                ('approvalCriteria', models.CharField(max_length=1500)),
                ('references', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=1500)),
                ('email', models.CharField(max_length=1500, unique=True)),
                ('password', models.CharField(max_length=1500)),
                ('phone', models.CharField(max_length=1500)),
                ('birthdate', models.DateTimeField()),
                ('profileType', models.IntegerField()),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=1500, unique=True)),
                ('name', models.CharField(max_length=1500)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserEvent',
            fields=[
                ('eventId', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('eventType', models.IntegerField()),
                ('classId', models.IntegerField()),
                ('teacherName', models.CharField(max_length=1500)),
                ('title', models.CharField(max_length=1500)),
                ('description', models.CharField(max_length=1500)),
                ('dateOfEvent', models.DateField()),
                ('timeOfEvent', models.TimeField()),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
                ('updatedBy', models.IntegerField()),
                ('status', models.CharField(max_length=1500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebAppEAD.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserClassroom',
            fields=[
                ('classroomId', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('className', models.CharField(max_length=1500)),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
                ('createdBy', models.IntegerField()),
                ('user', models.ManyToManyField(to='WebAppEAD.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserAssignment',
            fields=[
                ('assignmentId', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('identifier', models.IntegerField()),
                ('title', models.CharField(max_length=1500)),
                ('description', models.CharField(max_length=1500)),
                ('classId', models.IntegerField()),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
                ('createdBy', models.IntegerField()),
                ('updatedBy', models.IntegerField()),
                ('dueDate', models.DateTimeField()),
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
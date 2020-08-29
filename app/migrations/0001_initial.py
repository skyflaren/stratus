# Generated by Django 3.1 on 2020-08-29 03:53

import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of this badge.', max_length=48, verbose_name='name')),
                ('description', models.TextField(help_text='Description of this badge.', verbose_name='Description')),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', help_text='Color', max_length=18, verbose_name='The color of this tag.')),
                ('points', models.PositiveSmallIntegerField(help_text='Points awarded for this badge.', verbose_name='Points')),
                ('icon', models.ImageField(help_text='Icon of badge.', upload_to='badges/', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of this challenge.', max_length=100, verbose_name='Name')),
                ('description', models.TextField(help_text='Description of this badge.', verbose_name='Description')),
                ('created', models.DateField(auto_now_add=True, help_text='Date this challenge was created.', verbose_name='Creation Date')),
                ('start', models.DateTimeField(help_text='Start date and time when projects can be created for this challenge.', verbose_name='Challenge Start')),
                ('end', models.DateTimeField(help_text='End date and time when projects can no longer be created for this challenge.', verbose_name='Challenge End')),
                ('image', models.ImageField(help_text='Cover image of this challenge.', upload_to='challenges/', verbose_name='Image')),
                ('creators', models.ManyToManyField(help_text='Creators of this challenge which can edit its properties.', related_name='created_challenges', to=settings.AUTH_USER_MODEL, verbose_name='Creators')),
                ('rewards', models.ManyToManyField(help_text='Badges awareded to users that complete projects for this challenge.', related_name='challenges', to='app.Badge', verbose_name='Rewards')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='User description.', verbose_name='Description')),
                ('badges', models.ManyToManyField(help_text='Badges awarded to this user.', related_name='profiles', to='app.Badge', verbose_name='Badges')),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of this social link.', max_length=24, verbose_name='Name')),
                ('icon', models.ImageField(help_text='Icon of badge.', upload_to='badges/', verbose_name='Image')),
                ('site', models.CharField(help_text="Python format string which will have '%s' replaced with the link content.", max_length=2047, verbose_name='Site')),
                ('placeholder', models.CharField(help_text='Placeholder text displayed to the user when creating a link.', max_length=32, verbose_name='Placeholder')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of this tag.', max_length=24, verbose_name='Name')),
                ('category', models.CharField(choices=[('S', 'Skill'), ('L', 'Location'), ('K', 'Knowledge'), ('I', 'Importance')], help_text='Category of this tag which determines where it is available and presented.', max_length=1, verbose_name='Category')),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', help_text='Color', max_length=18, verbose_name='Color of this tag.')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(help_text='Status of this task.', max_length=1, verbose_name='Status')),
                ('tags', models.ManyToManyField(help_text='Tags associated with this task.', related_name='tags', to='app.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='TaskSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(help_text='Status of this submission.', max_length=1, verbose_name='Status')),
                ('description', models.TextField(help_text='Description of this badge.', verbose_name='Description')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='app.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='SocialLinkAttachement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(help_text='URL or username to be replaced in social link.', max_length=2047, verbose_name='Content')),
                ('object_id', models.PositiveIntegerField(verbose_name='Linked Item ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='Linked Item Type')),
                ('link', models.ForeignKey(help_text='Social link of this link attachment.', on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='app.sociallink', verbose_name='Link')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, help_text='Date this project was created.', verbose_name='Creation Date')),
                ('image', models.ImageField(help_text='Cover image of this project.', upload_to='challenges/', verbose_name='Image')),
                ('challenge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.challenge')),
                ('contributors', models.ManyToManyField(help_text='Those who have completed tasks for this project.', related_name='contributed_projects', to='app.Profile', verbose_name='Contributors')),
                ('creators', models.ManyToManyField(help_text='Creators of this project which can edit its properties.', related_name='created_projects', to='app.Profile', verbose_name='Creators')),
                ('tags', models.ManyToManyField(help_text='Tags associated with this project.', related_name='projects', to='app.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='tags',
            field=models.ManyToManyField(help_text='Tags associated with this user.', related_name='profiles', to='app.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='challenge',
            name='tags',
            field=models.ManyToManyField(help_text='Tags associated with this challenge.', related_name='challenges', to='app.Tag', verbose_name='Tags'),
        ),
    ]
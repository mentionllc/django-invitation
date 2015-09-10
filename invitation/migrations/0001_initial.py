# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InvitationKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=40, verbose_name='invitation key')),
                ('date_invited', models.DateTimeField(auto_now_add=True, verbose_name='date invited')),
                ('uses_left', models.IntegerField(default=1)),
                ('recipient', picklefield.fields.PickledObjectField(default=None, null=True, editable=False)),
                ('from_user', models.ForeignKey(related_name='invitations_sent', to=settings.AUTH_USER_MODEL)),
                ('registrant', models.ManyToManyField(related_name='invitations_used', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='InvitationUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invitations_remaining', models.IntegerField()),
                ('inviter', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]

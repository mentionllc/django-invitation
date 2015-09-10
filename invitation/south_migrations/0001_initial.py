# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InvitationKey'
        db.create_table('invitation_invitationkey', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('date_invited', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('from_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='invitations_sent', to=orm['auth.User'])),
            ('uses_left', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('invitation', ['InvitationKey'])

        # Adding M2M table for field registrant on 'InvitationKey'
        db.create_table('invitation_invitationkey_registrant', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('invitationkey', models.ForeignKey(orm['invitation.invitationkey'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('invitation_invitationkey_registrant', ['invitationkey_id', 'user_id'])

        # Adding model 'InvitationUser'
        db.create_table('invitation_invitationuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('inviter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('invitations_remaining', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('invitation', ['InvitationUser'])


    def backwards(self, orm):
        # Deleting model 'InvitationKey'
        db.delete_table('invitation_invitationkey')

        # Removing M2M table for field registrant on 'InvitationKey'
        db.delete_table('invitation_invitationkey_registrant')

        # Deleting model 'InvitationUser'
        db.delete_table('invitation_invitationuser')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'invitation.invitationkey': {
            'Meta': {'object_name': 'InvitationKey'},
            'date_invited': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invitations_sent'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'registrant': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'invitations_used'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'uses_left': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'invitation.invitationuser': {
            'Meta': {'object_name': 'InvitationUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invitations_remaining': ('django.db.models.fields.IntegerField', [], {}),
            'inviter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['invitation']
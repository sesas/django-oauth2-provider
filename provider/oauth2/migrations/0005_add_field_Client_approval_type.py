# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

from provider.compat import user_model_label


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Client.approval_type'
        db.add_column(u'oauth2_client', 'approval_type',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Client.approval_type'
        db.delete_column(u'oauth2_client', 'approval_type')


    models = {
        u'oauth2.accesstoken': {
            'Meta': {'object_name': 'AccessToken'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oauth2.Client']"}),
            'expires': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scope': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'token': ('django.db.models.fields.CharField', [], {'default': "'14763e0bad5d02f2ac7d51fb5c0c6b6fdef69119'", 'max_length': '255', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['%s']" % user_model_label})
        },
        u'oauth2.client': {
            'Meta': {'object_name': 'Client'},
            'approval_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'client_id': ('django.db.models.fields.CharField', [], {'default': "'c848f2f6be7ce376e9c9'", 'max_length': '255'}),
            'client_secret': ('django.db.models.fields.CharField', [], {'default': "'ff7d5957b5025cb7ed774cb60f446bba6fba14cd'", 'max_length': '255'}),
            'client_type': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'redirect_uri': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'oauth2_client'", 'null': 'True', 'to': "orm['%s']" % user_model_label})
        },
        u'oauth2.grant': {
            'Meta': {'object_name': 'Grant'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oauth2.Client']"}),
            'code': ('django.db.models.fields.CharField', [], {'default': "'f9bacfd07663f02162d5bc36919d2e034c71d85e'", 'max_length': '255'}),
            'expires': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 25, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'redirect_uri': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'scope': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['%s']" % user_model_label})
        },
        u'oauth2.refreshtoken': {
            'Meta': {'object_name': 'RefreshToken'},
            'access_token': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'refresh_token'", 'unique': 'True', 'to': u"orm['oauth2.AccessToken']"}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oauth2.Client']"}),
            'expired': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'default': "'7b2c01545958bbf53ccf17a09b5e109737ce07e0'", 'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['%s']" % user_model_label})
        },
        user_model_label: {
            'Meta': {'object_name': user_model_label.split('.')[-1], 'db_table': "'users'"},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'eid': ('django.db.models.fields.CharField', [], {'max_length': '22'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'force_two_factor_auth': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "'last_login_date'", 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'locale': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        }
    }

    complete_apps = ['oauth2']
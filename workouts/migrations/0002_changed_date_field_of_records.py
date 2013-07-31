# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Record.for_date'
        db.delete_column('workouts_record', 'for_date')

        # Adding field 'Record.date'
        db.add_column('workouts_record', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 7, 31, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Record.for_date'
        db.add_column('workouts_record', 'for_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 7, 31, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'Record.date'
        db.delete_column('workouts_record', 'date')


    models = {
        'workouts.record': {
            'Meta': {'object_name': 'Record'},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workouts.Workout']"})
        },
        'workouts.workout': {
            'Meta': {'object_name': 'Workout'},
            'current_streak': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'longest_streak': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['workouts']
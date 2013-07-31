# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Workout.color'
        db.add_column('workouts_workout', 'color',
                      self.gf('django.db.models.fields.CharField')(default='green', max_length=128),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Workout.color'
        db.delete_column('workouts_workout', 'color')


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
            'color': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'current_streak': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'longest_streak': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['workouts']
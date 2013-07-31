# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Workout'
        db.create_table('workouts_workout', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('current_streak', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('longest_streak', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('workouts', ['Workout'])

        # Adding model 'Record'
        db.create_table('workouts_record', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workouts.Workout'])),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
            ('for_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('workouts', ['Record'])


    def backwards(self, orm):
        # Deleting model 'Workout'
        db.delete_table('workouts_workout')

        # Deleting model 'Record'
        db.delete_table('workouts_record')


    models = {
        'workouts.record': {
            'Meta': {'object_name': 'Record'},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'for_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
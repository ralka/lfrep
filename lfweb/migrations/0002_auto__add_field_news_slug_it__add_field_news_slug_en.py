# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.slug_it'
        db.add_column(u'lfweb_news', 'slug_it',
                      self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.slug_en'
        db.add_column(u'lfweb_news', 'slug_en',
                      self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'News.slug_it'
        db.delete_column(u'lfweb_news', 'slug_it')

        # Deleting field 'News.slug_en'
        db.delete_column(u'lfweb_news', 'slug_en')


    models = {
        u'lfweb.collection': {
            'Meta': {'object_name': 'Collection'},
            'abstract': ('tinymce.models.HTMLField', [], {'max_length': '255', 'null': 'True'}),
            'abstract_en': ('tinymce.models.HTMLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'abstract_it': ('tinymce.models.HTMLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description': ('tinymce.models.HTMLField', [], {'null': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lfweb.Gallery']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True'}),
            'name_en': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'name_it': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lfweb.Collection']", 'null': 'True'}),
            'pub': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pub_order': ('django.db.models.fields.SmallIntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True'}),
            'title': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True'}),
            'title_en': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'title_it': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'video_url': ('django.db.models.fields.CharField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'})
        },
        u'lfweb.gallery': {
            'Meta': {'object_name': 'Gallery'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '130'})
        },
        u'lfweb.image': {
            'Meta': {'object_name': 'Image'},
            'abstract': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lfweb.Gallery']", 'null': 'True'}),
            'pub': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pub_order': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'lfweb.news': {
            'Meta': {'object_name': 'News'},
            'abstract': ('tinymce.models.HTMLField', [], {'max_length': '255', 'null': 'True'}),
            'abstract_en': ('tinymce.models.HTMLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'abstract_it': ('tinymce.models.HTMLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lfweb.Gallery']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pub_order': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True'}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug_it': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'text': ('tinymce.models.HTMLField', [], {'null': 'True'}),
            'text_en': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'text_it': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True'}),
            'title_en': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'title_it': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'video_url': ('django.db.models.fields.CharField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'})
        },
        u'lfweb.yarn': {
            'Meta': {'object_name': 'Yarn'},
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lfweb.Collection']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('tinymce.models.HTMLField', [], {'max_length': '130'}),
            'name_en': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'name_it': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'pub': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pub_order': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True'}),
            'title': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'title_en': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'title_it': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['lfweb']
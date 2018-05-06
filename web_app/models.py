# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Information(models.Model):
    w_id = models.AutoField(primary_key=True)
    nickname = models.CharField(db_column='NickName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    num_fans = models.IntegerField(db_column='Num_Fans', blank=True, null=True)  # Field name made lowercase.
    num_follows = models.IntegerField(db_column='Num_Follows', blank=True, null=True)  # Field name made lowercase.
    num_tweets = models.IntegerField(db_column='Num_Tweets', blank=True, null=True)  # Field name made lowercase.
    create_time = models.TimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'information'


class Tweets(models.Model):
    wb_id = models.AutoField(primary_key=True)
    content = models.CharField(db_column='Content', max_length=400, blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='NickName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comment = models.IntegerField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    like = models.IntegerField(db_column='Like', blank=True, null=True)  # Field name made lowercase.
    pubtime = models.CharField(db_column='PubTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transfer = models.IntegerField(db_column='Transfer', blank=True, null=True)  # Field name made lowercase.
    create_time = models.TimeField(blank=True, null=True)
    up_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tweets'

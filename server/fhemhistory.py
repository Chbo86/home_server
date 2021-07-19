# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class History(models.Model):
    timestamp = models.DateTimeField(db_column='TIMESTAMP')  # Field name made lowercase.
    device = models.CharField(db_column='DEVICE', max_length=64, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=64, blank=True, null=True)  # Field name made lowercase.
    event = models.CharField(db_column='EVENT', max_length=512, blank=True, null=True)  # Field name made lowercase.
    reading = models.CharField(db_column='READING', max_length=64, blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='VALUE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='UNIT', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'history'

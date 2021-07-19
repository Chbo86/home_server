from django.db import models

# Create your models here.

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

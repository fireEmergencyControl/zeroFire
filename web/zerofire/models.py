from django.db import models

# Create your models here.
class Manager(models.Model):
    mno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pass_field = models.CharField(db_column='pass', max_length=20, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    rno = models.ForeignKey('Rankdata', models.DO_NOTHING, db_column='rno', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'manager'


class Rankdata(models.Model):
    rno = models.IntegerField(primary_key=True)
    rankdata = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rankdata'
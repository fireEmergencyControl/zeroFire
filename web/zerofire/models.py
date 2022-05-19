from django.db import models

# Create your models here.
class Manager(models.Model):
    mno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=100, blank=True)
    workarea = models.CharField(max_length=25)
    id = models.CharField(db_column='ID', max_length=20)  # Field name made lowercase.
    mgr_pass = models.CharField(db_column='PW', max_length=20)  # Field renamed because it was a Python reserved word.
    rno = models.ForeignKey('Rankdata', models.DO_NOTHING, db_column='rno')

    class Meta:
        db_table = 'manager'


class Rankdata(models.Model):
    rno = models.IntegerField(primary_key=True)
    rankdata = models.CharField(max_length=10, blank=True)

    class Meta:
        db_table = 'rankdata'


class Board(models.Model):
    bno = models.AutoField(primary_key=True)
    mno = models.ForeignKey('Manager', models.DO_NOTHING, db_column='mno', blank=True, null=True)
    fire_count = models.IntegerField(blank=True, null=True)
    pump = models.CharField(max_length=10, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    etc = models.CharField(max_length=500, blank=True, null=True)
    regdate = models.DateTimeField()

    class Meta:
        db_table = 'board'

class Reply(models.Model):
    rno = models.AutoField(primary_key=True)
    cno = models.ForeignKey(Board, models.DO_NOTHING, db_column='cno', blank=True, null=True)
    content = models.CharField(max_length=50, blank=True, null=True)
    reg_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'reply'
from django.db import models

# Create your models here.
class Manager(models.Model):
    mno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=100, blank=True)
    workarea = models.CharField(max_length=25)
    id = models.CharField(db_column='ID', max_length=20)  # Field name made lowercase.
    pass_field = models.CharField(db_column='pass', max_length=20)  # Field renamed because it was a Python reserved word.
    rno = models.ForeignKey('Rankdata', models.DO_NOTHING, db_column='rno')

    class Meta:
        db_table = 'manager'


class Rankdata(models.Model):
    rno = models.IntegerField(primary_key=True)
    rankdata = models.CharField(max_length=10, blank=True)

    class Meta:
        db_table = 'rankdata'
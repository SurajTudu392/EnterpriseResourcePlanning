from django.db import models

# Create your models here.
class Students(models.Model):
    id=models.IntegerField(primary_key=True)
    username=models.CharField()
    enrollment=models.BigIntegerField()
    semester=models.IntegerField()
    branch=models.CharField(max_length=200,null=True)
    

class Subjects(models.Model):
    id=models.AutoField(primary_key=True)
    subjectname=models.CharField()
    code=models.BigIntegerField()
    semester=models.IntegerField()
    

class AttendanceRecord(models.Model):
    id=models.AutoField(primary_key=True)
    student=models.ForeignKey('Students',on_delete=models.CASCADE)
    subject=models.ForeignKey('Subjects',on_delete=models.CASCADE)
    date=models.DateField()
    status=models.IntegerField(max_length=1)
    timestamp=models.DateTimeField()

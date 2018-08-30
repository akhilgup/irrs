from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    emp_id = models.TextField(db_column='emp_id', max_length=10)
    emp_name = models.TextField(db_column='emp_name', max_length=100)
    creds = models.TextField(db_column='credentials', max_length=50) # password like details
    desg = models.TextField(db_column='designation', max_length=20) # Employee designation

    class Meta:
        managed = True
        db_table = 'Employee Details'

class Worker(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    worker_id = models.TextField(db_column='emp_id', max_length=10)
    worker_name = models.TextField(db_column='emp_name', max_length=100)
    mobile = models.IntegerField(db_column='mobile no.')
    desg = models.TextField(db_column='designation', max_length=20) # Worker
    assigned_by = models.ForeignKey('Employee',db_column='empId',on_delete=models.CASCADE)
    status = models.TextField(db_column='status', max_length=20) # Assigned or unassigned

    class Meta:
        managed = True
        db_table = 'Worker Details'

class User(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    uid = models.TextField(db_column='User ID', max_length=50) # user ID
    creds = models.TextField(db_column='credentials', max_length=50) # user password

    class Meta:
        managed = True
        db_table = 'Users'

class Complains(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    title = models.TextField(db_column='title', max_length=200) # complaint title
    text = models.TextField(db_column='text', max_length=1000) # complaint text
    image = models.TextField(db_column='image', max_length=500000) # base64 encoded string
    location = models.TextField(db_column='location', max_length=100) # location of the problem
    compl_by = models.TextField(db_column='user', max_length=50)
    # compl_by = models.ForeignKey('User',db_column='user_id',on_delete=models.CASCADE) # who registered the complaint
    status = models.TextField(db_column='status', max_length=200) # status of the registered complaint, processed or not

    class Meta:
        managed = True
        db_table = 'Complaints'

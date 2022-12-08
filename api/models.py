from django.db import models

# Create your models here.

class Company(models.Model):
    company_id   =     models.AutoField(primary_key=True)
    name         =     models.CharField(max_length=100)
    location     =     models.CharField(max_length=60)
    about        =     models.TextField()
    type         =     models.CharField(max_length=100, choices=(('IT', 'IT'),('Non-IT', 'Non-IT'),('Mobile Phone', 'Mobile Phone')))
    date         =     models.DateField(auto_now=True)
    active       =     models.BooleanField(default=True)

    def __str__(self):
        return self.name



#Employee Model

class Employee(models.Model):
    employee_id        = models.AutoField(primary_key=True)
    name               = models.CharField(max_length=100)
    email              = models.CharField(max_length=60)
    address            = models.CharField(max_length=100)
    phone              = models.CharField(max_length=20)
    about              = models.TextField()
    position           = models.CharField(max_length=60, choices=(
        ('SoftwareDeveloper', 'SD'),
        ('Manager', 'Manager'),
        ('TeamLeader', 'TL')
    ))
    company            = models.ForeignKey(Company, on_delete=models.CASCADE)

    


    
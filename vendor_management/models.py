from django.db import models

# Create your models here.


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=200)

    def __str__(self):
        return self.vendor_name


class Contract(models.Model):
    contract_name = models.CharField(max_length=200)
    contract_type = (
        ('MSA', 'Master Agreement'),
        {'AME', 'Amendment'}
    )
    contract_vendor = models.ForeignKey(
        'Vendor'
    )

    def __str__(self):
        return self.contract_name


class Service(models.Model):
    service_name = models.CharField(max_length=200)
    service_contract = models.ForeignKey(
        'Contract'
    )

    def __str__(self):
        return self.service_name


class User(models.Model):
    user_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    department = models.ForeignKey(
        'Department'
    )
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.user_name


class Department(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_contract = models.ForeignKey(
        'Contract'
    )

    def __str__(self):
        return self.project_name


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    duration = models.DurationField
    hours = models.DurationField
    task_project = models.ForeignKey(
        'Project'
    )

    def __str__(self):
        return self.task_name

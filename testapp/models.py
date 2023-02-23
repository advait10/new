from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class Employee(models.Model):
    company_name = models.CharField(max_length=30)
    email_id = models.CharField(max_length=30)
    company_code = models.CharField(max_length=50,validators=[alphanumeric])
    strength = models.IntegerField()
    website = models.URLField()
    created_time = models.TimeField(auto_now=True)


    class Meta:
        db_table = 'emp'
# Create your models here.

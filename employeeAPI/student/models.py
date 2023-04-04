from django.db import models

# Create your models here.
class Student(models.Model):
    reg_no = models.TextField(unique=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    mobile = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
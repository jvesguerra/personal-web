# myapp/models.py
from django.db import models

class Person(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    class Meta:
        db_table = 'people'  # Ensure this is set to the actual table name

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
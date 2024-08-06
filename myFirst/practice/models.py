from django.db import models

STATUS_CHOICES = [
    ("f","FSC"),
    ("m", "MATRIC"),
    ("g", "Graduation"),
]
class Student(models.Model):
    name= models.CharField(max_length=10)
    email= models.EmailField(unique=True)
    status=models.CharField(max_length=1, choices=STATUS_CHOICES, null=True)

    def __str__(self) -> str:
        return self.name
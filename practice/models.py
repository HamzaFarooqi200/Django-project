from django.db import models

STATUS_CHOICES = [
    ("f","FSC"),
    ("m", "MATRIC"),
    ("g", "Graduation"),
]
class Student(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, null = True)
    is_sportsman = models.BooleanField(default = False)
    is_speaker = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.name


class SportsmanManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_sportsman=True)
    
class Sportsman(Student):
    objects = SportsmanManager()

    class Meta():
        proxy = True
    
    def save(self, *args, **kwargs):
        kwargs['is_sportsman'] = True
        return super().save(*args, **kwargs)


class SpeakerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_speaker=True)
    
class Speaker(Student):
    objects = SpeakerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        kwargs['is_speaker'] = True
        return super().save(*args, **kwargs)
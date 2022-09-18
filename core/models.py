from django.db import models
from django.utils import timezone

class Patient(models.Model):
    genre_choices = (
        ('Femme', 'Femme'),
        ("Homme", "Homme")
    )
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField()
    adresse = models.CharField(max_length=200)
    numero_de_telephone = models.PositiveIntegerField()
    observations = models.TextField()
    genre = models.CharField(max_length=10, choices=genre_choices)
    prescriptions = models.CharField(max_length=200)
    date_created = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"

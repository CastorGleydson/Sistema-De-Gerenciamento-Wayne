from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = (
        ('employee', 'Funcionário'),
        ('manager', 'Gerente'),
        ('admin', 'Administrador'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='employee')

class Resource(models.Model):
    CATEGORIES = (
        ('equipment', 'Equipamento'),
        ('vehicle', 'Veículo'),
        ('device', 'Dispositivo'),
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    status = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
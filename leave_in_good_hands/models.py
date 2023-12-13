
from django.db import models

from accounts.models import MyUser


# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Institution(models.Model):
    institution_choices = [
        ('fundacja', 'Fundacja'),
        ('organizacja_pozarzadowa', 'Organizacja pozarządowa'),
        ('zbiorka_lokalna', 'Zbiórka lokalna'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=64, choices=institution_choices, default='fundacja')
    categories = models.ManyToManyField(Category, related_name='institutions')

    def __str__(self):
        return self.name.filter(type="")

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category, related_name='donations')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='donation_institution')
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField(max_length=250, blank=True, null=True)
    user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Donation {self.id} - {self.quantity}"
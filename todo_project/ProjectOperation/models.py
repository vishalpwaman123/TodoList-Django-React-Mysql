from django.db import models

# Create your models here.


class product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stars = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




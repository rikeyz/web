from django.db import models


class Menu(models.Model):
    catetoryname = models.CharField(max_length=20)
    unique_code = models.CharField(max_length=32)


from django.db import models

class Survey(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    survey_date = models.DateField()
    liked_most = models.CharField(max_length=255)
    interest_source = models.CharField(max_length=255)
    recommend_likelihood = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

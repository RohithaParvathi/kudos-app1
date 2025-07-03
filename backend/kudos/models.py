from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

class Kudos(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kudos_given')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kudos_received')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

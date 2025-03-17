from django.db import models

class Folder(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class PasswordEntry(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=255)
    site_link = models.URLField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    extra_fields = models.JSONField(default=dict, blank=True)  

    def __str__(self):
        return self.site_name

from __future__ import unicode_literals
from django.db import models

class add(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) <3:
            errors["title"] = "Blog name should be at least 2 characters"
        if len(postData['network']) < 4:
            errors["network"] = "Blog name should be at least 3 characters"
        if len(postData['description']) < 10:
            errors["description"] = "Blog description should be at least 10 characters"
        return errors

class tv(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = add()



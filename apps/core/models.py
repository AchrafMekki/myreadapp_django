from django.db import models

# Create your models here.


class CreatedModifiedAbstract(models.Model):
    #  this should default to the currentdate and time
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    # This should be change each time in a row 
    modified_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
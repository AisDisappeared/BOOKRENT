from django.db import models
from django_countries.fields import CountryField
import uuid 


class Publisher(models.Model):
    # book publisher 
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    name = models.CharField(max_length=255)
    country = CountryField(blank_label="(select country)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} from {self.country}"
    

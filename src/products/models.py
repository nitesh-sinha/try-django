from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100) # max_length is required field
    description = models.TextField(blank=True, null=True) # blank=true means its an optional field while adding new products. Null=true means DB can store null value for this field.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    summary = models.TextField(default="THis is a default summary")
    featured = models.BooleanField(blank=True, default=False)

    def get_absolute_urls(self):
        #return f"/products/{self.id}"
        # More dynamic way of generating the product URL using path "name" in urls.py
        return reverse("products:product-detail", kwargs={"my_id": self.id}) # <app_name>:<path_name> in urls.py
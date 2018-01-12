from django.db import models

# Create your models here.

"""
Only admin users can add or delete products.
Users can view all products.
Users can buy a product.
Users should be able to provide rating(1-5) to a product they've bought. They should not be able to add rating to any other product.
Users should be able to change their rating for a product.
While querying for a product it should also return the average rating along with product details.
"""


OPTIONAL = {"blank": True, "null": True}
ACTIVE = ((0, 'Inactive'), (2, 'Active'))


class BaseContent(models.Model):
    """BaseContent to created the Common Fields."""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.IntegerField(choices=ACTIVE, default=2)

    class Meta:
        """Making Common Class for other Models."""

        abstract = True


class Location(BaseContent):
    """This Model Class to Store Location Names."""

    name = models.CharField(max_length=100, **OPTIONAL)
    latitude = models.TextField()
    longitude = models.TextField()

    def __str__(self):
        """Return Location name."""
        return self.name


class Product(BaseContent):
    """To store Product Information."""

    name = models.TextField()
    image = models.ImageField(upload_to="static/%y/%m/%d/", **OPTIONAL)
    description = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        """Return Product name."""
        return self.name


class UserProduct(BaseContent):
    """To Know which product brought by user."""

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, **OPTIONAL)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, **OPTIONAL)

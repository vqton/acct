from django.db import models


class Customer(models.Model):
    """
    Represents a customer (company or similar entity) in the accounting system.
    """

    # Basic information
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    # Financial details
    account_balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    credit_limit = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)

    # Other relevant fields (you can customize as needed)
    tax_id = models.CharField(
        max_length=20, blank=True, null=False, primary_key=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

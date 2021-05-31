from django.db import models
from django_db_views.db_view import DBView


class Bank(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=49, help_text="Name of the bank")
            
    def __str__(self):
        return self.name

    
class Branch(models.Model):
    
    ifsc = models.CharField(primary_key=True, max_length=21,
                            help_text="IFSC code of branch")

    bank = models.ForeignKey(Bank,related_name='branches',  on_delete=models.CASCADE, help_text="FK to Bank table")

    branch = models.CharField(max_length=74, help_text="Area of the branch is located")

    address = models.CharField(max_length=195, help_text="Detailed address of the branch")

    city = models.CharField(max_length=50, help_text="City where branch is located")

    district = models.CharField(max_length=50, help_text="District where branch is located")

    state = models.CharField(max_length=26, help_text="State in which branch is located")

    def __str__(self):
        return 'ifsc: {}, bank:{}, branch'.format(self.ifsc, self.bank, self.branch)


   
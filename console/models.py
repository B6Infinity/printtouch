from django.db import models
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import CharField, TextField


class Account(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    amt_present = models.PositiveBigIntegerField(default=0)

    category_choices = (
        ('cc', 'cc'),
        ('hbl', 'hbl'),
        ('savings', 'savings'),
        ('joint', 'joint'),
    )

    category = models.CharField(max_length=25, choices=category_choices, default='cc')

    pd_upcoming_date = models.DateField(null=True, blank=True)
    pd_amt = models.PositiveIntegerField(null=True, blank=True)
    

    def __str__(self) -> str:
        return f"{self.name} - {self.category}"


class Flow(models.Model):
    depwith_choices = (
        ('deposit', 'deposit'),
        ('withdraw', 'withdraw'),
    )

    flow = models.CharField(max_length=25, choices=depwith_choices, default='withdraw')

    is_cheque = models.BooleanField(default=False)
    catalyst = models.CharField(max_length=50)
    purpose = models.CharField(max_length=100)
    
    amount = models.PositiveBigIntegerField(default=0)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} - {self.flow} by {self.catalyst} [{self.time_created.date().strftime('%Y-%m-%d, %H:%M %p')}]"
    

    


# class Customer(models.Model):
#     name = models.CharField(max_length=120)
#     phone_no =  models.IntegerField()

#     address = models.TextField(default="")

#     def __str__(self) -> str:
#         return f"{self.name}({self.phone_no})"
from django.db import models

class Transaction(models.Model):
   transDate          = models.DateField()
   transAmmount       = models.DecimalField(decimal_places=3)
   transDescription   = models.CharField(max_length=100)
   accountId          = models.ForeignKey(Account)
   vendorId           = models.ForeignKey(Vendor)
   categoryID         = models.ForeignKey(Category)

class Account(models.Model):
   acctName    = models.CharField(max_length=50)
   acctNumber  = models.IntegerField(max_length=25)
   acctType    = models.CharField(max_length=50)   #should be a custom field with options checking savings creditcard etc
   bankId      = models.ForeignKey(Bank)

class Bank:
   bankName       = models.CharField(max_length=50)
   bankRoutingNum = models.IntegerField(max_length=10)

class Vendor(models.Model):
   vendorName           = models.CharField(max_length=50)
   vendorAddress        = models.CharField(max_length=50)
   vendorCity           = models.CharField(max_length=60)
   vendorState_province = models.CharField(max_length=30)
   vendorCountry        = models.CharField(max_length=50)
   vendorWebsite        = models.URLField()

class Category(models.Model):
  catName        = models.CharField(max_length=50)
  catDescription = models.CharField(max_length=100)
  catSubCat      = models.ForeignKey(Category)

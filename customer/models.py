# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


#   Rent Cards
#   Domain:
#
#   Author: Jan Dusek
#   E-mail: honzikd@gmail.com
#   
#
#   The purpose of this file is to define classed used to model the basic
#   entity - a customer
#

class Customer(models.Model):
    user = models.ForeignKey(User, unique=True)
    first_name = models.CharField("Jméno", max_length=50)
    last_name = models.CharField("Příjmení", max_length=50)
    address = models.CharField("Ulice, č.p.", max_length=100)
    city = models.CharField("Město", max_length=30)
    zip = models.IntegerField("PSČ")
    date_of_birth = models.DateField("Datum narození")
    
    
    def __unicode__(self):
        return self.last_name + " - " + str(self.date_of_birth)
        
    class Meta:
        verbose_name = "Zákazník"
        verbose_name_plural = "Zákazníci"
        
        
class Card(models.Model):
    card_number = models.IntegerField("Číslo karty", unique=True)
    parent_customer = models.ForeignKey("Customer")
    
    def __unicode__(self):
        return str(self.card_number) + " - " + self.parent_customer.__unicode__()
        
    class Meta:
        verbose_name = "Karta"
        verbose_name_plural = "Karty"
        
try: 
    admin.site.register(Customer)
    admin.site.register(Card)
except:
    pass
        
        

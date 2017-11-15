# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField()

    def __str__(self):
        return str(self.email)

    def __unicode__(self):
        return unicode(self.email)


class Compose(models.Model):
    fromemail=models.EmailField()
    sendto=models.ForeignKey(Person)
    subject=models.CharField(max_length=100)
    content=models.TextField(max_length=500)

    def __str__(self):
        return str(self.sendto)

    def __unicode__(self):
        return unicode(self.sendto)

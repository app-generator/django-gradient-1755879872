# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Rekening(models.Model):

    #__Rekening_FIELDS__
    rekeningnummer = models.TextField(max_length=255, null=True, blank=True)
    rekening = models.TextField(max_length=255, null=True, blank=True)
    beginsaldo = models.IntegerField(null=True, blank=True)

    #__Rekening_FIELDS__END

    class Meta:
        verbose_name        = _("Rekening")
        verbose_name_plural = _("Rekening")


class Transactie(models.Model):

    #__Transactie_FIELDS__
    rekeningnummer = models.ForeignKey(rekening, on_delete=models.CASCADE)
    bedrag = models.IntegerField(null=True, blank=True)
    datum = models.DateTimeField(blank=True, null=True, default=timezone.now)
    categorie_id = models.ForeignKey(categorie, on_delete=models.CASCADE)

    #__Transactie_FIELDS__END

    class Meta:
        verbose_name        = _("Transactie")
        verbose_name_plural = _("Transactie")


class Categorie(models.Model):

    #__Categorie_FIELDS__
    categorie_id = models.IntegerField(null=True, blank=True)
    categorie = models.TextField(max_length=255, null=True, blank=True)

    #__Categorie_FIELDS__END

    class Meta:
        verbose_name        = _("Categorie")
        verbose_name_plural = _("Categorie")



#__MODELS__END

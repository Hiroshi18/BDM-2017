# Standard Library
from datetime import date

# Django
from django.db import models

# Local Django
from database.models import ManifEnt


class ItemEnt(models.Model):
    identifier = models.CharField(max_length=1000, blank=True, null=True)
    itemIdentifier = models.CharField(max_length=1000, blank=True, null=True)
    fingerprint = models.CharField(max_length=1000, blank=True, null=True)
    provenanceOfTheItem = models.CharField(max_length=1000, blank=True, null=True)
    marksInscriptions = models.CharField(max_length=1000, blank=True, null=True)
    exhibitionHistory = models.CharField(max_length=1000, blank=True, null=True)
    conditionOfTheItem = models.CharField(max_length=1000, blank=True, null=True)
    treatmentHistory = models.CharField(max_length=1000, blank=True, null=True)
    scheduledTreatment = models.CharField(max_length=1000, blank=True, null=True)
    accessRestrictionsOnTheItem = models.CharField(max_length=1000, blank=True, null=True)
    locationOfItem = models.CharField(max_length=1000, blank=True, null=True)
    custodialHistoryOfItem = models.CharField(max_length=1000, blank=True, null=True)
    immediateSourceOfAcquisitionOfItem = models.CharField(max_length=1000, blank=True, null=True)
    relatedManifEnt = models.ForeignKey(ManifEnt, related_name="relatedManifEnt")

    def __unicode__(self):
        return '%s' % self.itemIdentifier

    def __str__(self):
        return '%s' % self.itemIdentifier


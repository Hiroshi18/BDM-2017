# Standard Library
from datetime import date

# Django
from django.db import models

# Local Django


class WorkEnt(models.Model):
    identifier = models.CharField(max_length=1000, blank=False, null=True)
    titleOfTheWork = models.CharField(max_length=1000, blank=False, null=True)
    formOfWork = models.CharField(max_length=1000, blank=False, null=True)
    dateOfTheWork = models.DateField(blank=False, default=date.today)

    otherDistinguishingCharacteristic = models.CharField(max_length=1000, blank=True, null=True)
    intendedTermination = models.CharField(max_length=1000, blank=True, null=True)
    intendedAudience = models.CharField(max_length=1000, blank=True, null=True)
    contextForTheWork = models.CharField(max_length=1000, blank=True, null=True)
    mediumOfPerformance = models.CharField(max_length=1000, blank=True, null=True)
    numericDesignation = models.CharField(max_length=1000, blank=True, null=True)
    key = models.CharField(max_length=1000, blank=True, null=True)
    coordinates = models.CharField(max_length=1000, blank=True, null=True)
    equinox = models.CharField(max_length=1000, blank=True, null=True)
    subjectOfTheWork = models.CharField(max_length=1000, blank=True, null=True)
    placeOfOriginOfTheWork = models.CharField(max_length=1000, blank=True, null=True)
    history = models.CharField(max_length=1000, blank=True, null=True)

    relatedExprList = models.ManyToManyField(
        'ExprEnt',
        related_name='relatedExprList',
        blank=True,
    )

    def __unicode__(self):
        return '%s' % self.titleOfTheWork

    def __str__(self):
        return '%s' % self.titleOfTheWork


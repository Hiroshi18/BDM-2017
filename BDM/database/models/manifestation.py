# Standard Library
from datetime import date

# Django
from django.db import models

# Local Django
from database.models import ExprEnt


class ManifEnt(models.Model):
    identifier = models.CharField(max_length=1000, blank=False, null=True)
    titleOfTheManifestation = models.CharField(max_length=1000, blank=False, null=True)
    dateOfPublicationDistribution = models.DateField(blank=False, default=date.today)
    placeOfPublicationDistribution = models.CharField(max_length=1000, blank=False, null=True)
    relatedExprEnt = models.ForeignKey(ExprEnt, related_name="relatedExprEnt")

    statementOfResponsibility = models.CharField(max_length=1000, blank=True, null=True)
    editionIssueDesignation = models.CharField(max_length=1000, blank=True, null=True)
    publisherDistributor = models.CharField(max_length=1000, blank=True, null=True)
    fabricatorManufacturer = models.CharField(max_length=1000, blank=True, null=True)
    seriesStatement = models.CharField(max_length=1000, blank=True, null=True)
    formOfCarrier = models.CharField(max_length=1000, blank=True, null=True)
    extentOfTheCarrier = models.CharField(max_length=1000, blank=True, null=True)
    physicalMedium = models.CharField(max_length=1000, blank=True, null=True)
    captureMode = models.CharField(max_length=1000, blank=True, null=True)
    dimensionsOfTheCarrier = models.CharField(max_length=1000, blank=True, null=True)
    manifestationIdentifier = models.CharField(max_length=1000, blank=True, null=True)
    sourceForAcquisitionAccessAuthorization = models.CharField(max_length=1000, blank=True, null=True)
    termsOfAvailability = models.CharField(max_length=1000, blank=True, null=True)
    accessRestrictionsOnTheManifestation = models.CharField(max_length=1000, blank=True, null=True)
    typeface = models.CharField(max_length=1000, blank=True, null=True)
    typeSize = models.CharField(max_length=1000, blank=True, null=True)
    foliation = models.CharField(max_length=1000, blank=True, null=True)
    collation = models.CharField(max_length=1000, blank=True, null=True)
    publicationStatus = models.CharField(max_length=1000, blank=True, null=True)
    numbering = models.CharField(max_length=1000, blank=True, null=True)
    playingSpeed = models.CharField(max_length=1000, blank=True, null=True)
    grooveWidth = models.CharField(max_length=1000, blank=True, null=True)
    kindOfCutting = models.CharField(max_length=1000, blank=True, null=True)
    tapeConfiguration = models.CharField(max_length=1000, blank=True, null=True)
    kindOfSound = models.CharField(max_length=1000, blank=True, null=True)
    specialReproductionCharacteristic = models.CharField(max_length=1000, blank=True, null=True)
    colour = models.CharField(max_length=1000, blank=True, null=True)
    reductionRatio = models.CharField(max_length=1000, blank=True, null=True)
    polarity = models.CharField(max_length=1000, blank=True, null=True)
    generation = models.CharField(max_length=1000, blank=True, null=True)
    presentationFormat = models.CharField(max_length=1000, blank=True, null=True)
    systemRequirements = models.CharField(max_length=1000, blank=True, null=True)
    fileCharacteristics = models.CharField(max_length=1000, blank=True, null=True)
    modeOfAccess = models.CharField(max_length=1000, blank=True, null=True)
    accessAddress = models.CharField(max_length=1000, blank=True, null=True)

    relatedItemList = models.ManyToManyField(
        'ItemEnt',
        related_name='relatedItemList',
        blank=True,
    )

    def __unicode__(self):
        return '%s' % self.titleOfTheManifestation

    def __str__(self):
        return '%s' % self.titleOfTheManifestation

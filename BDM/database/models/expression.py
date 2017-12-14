# Standard Library
from datetime import date

# Django
from django.db import models

# Local Django
from database.models import WorkEnt


class ExprEnt(models.Model):
    identifier = models.CharField(max_length=1000, blank=True, null=True)
    titleOfTheExpression = models.CharField(max_length=1000, blank=True, null=True)
    formOfExpression = models.CharField(max_length=1000, blank=True, null=True)
    dateOfExpression = models.DateField(blank=False, default=date.today)
    languageOfExpression = models.CharField(max_length=1000, blank=True, null=True)
    otherDistinguishingCharacteristic = models.CharField(max_length=1000, blank=True, null=True)
    extensibilityOfExpression = models.CharField(max_length=1000, blank=True, null=True)
    revisabilityOfExpression = models.CharField(max_length=1000, blank=True, null=True)
    extentOfTheExpression = models.CharField(max_length=1000, blank=True, null=True)
    summarizationOfContent = models.CharField(max_length=1000, blank=True, null=True)
    contextForTheExpression = models.CharField(max_length=1000, blank=True, null=True)
    criticalResponseToTheExpression = models.CharField(max_length=1000, blank=True, null=True)
    useRestrictionsOnTheExpression = models.CharField(max_length=1000, blank=True, null=True)
    sequencingPattern = models.CharField(max_length=1000, blank=True, null=True)
    expectedRegularityOfIssue = models.CharField(max_length=1000, blank=True, null=True)
    expectedFrequencyOfIssue = models.CharField(max_length=1000, blank=True, null=True)
    typeOfScore = models.CharField(max_length=1000, blank=True, null=True)
    mediumOfPerformance = models.CharField(max_length=1000, blank=True, null=True)
    scale = models.CharField(max_length=1000, blank=True, null=True)
    projection = models.CharField(max_length=1000, blank=True, null=True)
    presentationTechnique = models.CharField(max_length=1000, blank=True, null=True)
    representationOfRelief = models.CharField(max_length=1000, blank=True, null=True)
    geodeticGridAndVerticalMeasurement = models.CharField(max_length=1000, blank=True, null=True)
    recordingTechnique = models.CharField(max_length=1000, blank=True, null=True)
    specialCharacteristic = models.CharField(max_length=1000, blank=True, null=True)
    technique = models.CharField(max_length=1000, blank=True, null=True)
    relatedWorkEnt = models.ForeignKey(WorkEnt, related_name="relatedWorkEnt")

    relatedManifList = models.ManyToManyField(
        'ManifEnt',
        related_name='relatedManifList',
        blank=True,
    )

    def __unicode__(self):
        return '%s' % self.titleOfTheExpression

    def __str__(self):
        return '%s' % self.titleOfTheExpression

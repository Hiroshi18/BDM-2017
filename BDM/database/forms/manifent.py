# django
from django import forms

# local django
from database.models import WorkEnt


class CreateManifEntForm(forms.Form):
    identifier = forms.CharField(max_length=1000, blank=True, null=True)
    titleOfTheManifestation = forms.CharField(max_length=1000, blank=True, null=True)
    statementOfResponsibility = forms.CharField(max_length=1000, blank=True, null=True)
    editionIssueDesignation = forms.CharField(max_length=1000, blank=True, null=True)
    placeOfPublicationDistribution = forms.CharField(max_length=1000, blank=True, null=True)
    publisherDistributor = forms.CharField(max_length=1000, blank=True, null=True)
    dateOfPublicationDistribution = forms.CharField(max_length=1000, blank=True, null=True)
    fabricatorManufacturer = forms.CharField(max_length=1000, blank=True, null=True)
    seriesStatement = forms.CharField(max_length=1000, blank=True, null=True)
    formOfCarrier = forms.CharField(max_length=1000, blank=True, null=True)
    extentOfTheCarrier = forms.CharField(max_length=1000, blank=True, null=True)
    physicalMedium = forms.CharField(max_length=1000, blank=True, null=True)
    captureMode = forms.CharField(max_length=1000, blank=True, null=True)
    dimensionsOfTheCarrier = forms.CharField(max_length=1000, blank=True, null=True)
    manifestationIdentifier = forms.CharField(max_length=1000, blank=True, null=True)
    sourceForAcquisitionAccessAuthorization = forms.CharField(max_length=1000, blank=True, null=True)
    termsOfAvailability = forms.CharField(max_length=1000, blank=True, null=True)
    accessRestrictionsOnTheManifestation = forms.CharField(max_length=1000, blank=True, null=True)
    typeface = forms.CharField(max_length=1000, blank=True, null=True)
    typeSize = forms.CharField(max_length=1000, blank=True, null=True)
    foliation = forms.CharField(max_length=1000, blank=True, null=True)
    collation = forms.CharField(max_length=1000, blank=True, null=True)
    publicationStatus = forms.CharField(max_length=1000, blank=True, null=True)
    numbering = forms.CharField(max_length=1000, blank=True, null=True)
    playingSpeed = forms.CharField(max_length=1000, blank=True, null=True)
    grooveWidth = forms.CharField(max_length=1000, blank=True, null=True)
    kindOfCutting = forms.CharField(max_length=1000, blank=True, null=True)
    tapeConfiguration = forms.CharField(max_length=1000, blank=True, null=True)
    kindOfSound = forms.CharField(max_length=1000, blank=True, null=True)
    specialReproductionCharacteristic = forms.CharField(max_length=1000, blank=True, null=True)
    colour = forms.CharField(max_length=1000, blank=True, null=True)
    reductionRatio = forms.CharField(max_length=1000, blank=True, null=True)
    polarity = forms.CharField(max_length=1000, blank=True, null=True)
    generation = forms.CharField(max_length=1000, blank=True, null=True)
    presentationFormat = forms.CharField(max_length=1000, blank=True, null=True)
    systemRequirements = forms.CharField(max_length=1000, blank=True, null=True)
    fileCharacteristics = forms.CharField(max_length=1000, blank=True, null=True)
    modeOfAccess = forms.CharField(max_length=1000, blank=True, null=True)
    accessAddress = forms.CharField(max_length=1000, blank=True, null=True)
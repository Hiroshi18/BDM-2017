# Django
from django import forms

# Local Django
from database.models import ExprEnt, ManifEnt


class CreateManifEntForm(forms.ModelForm):
    class Meta:
        model = ManifEnt
        exclude = ('relatedItemList',)

    identifier = forms.CharField(max_length=1000, required=False, )
    titleOfTheManifestation = forms.CharField(max_length=1000, required=False, )
    statementOfResponsibility = forms.CharField(max_length=1000, required=False, )
    editionIssueDesignation = forms.CharField(max_length=1000, required=False, )
    placeOfPublicationDistribution = forms.CharField(max_length=1000, required=False, )
    publisherDistributor = forms.CharField(max_length=1000, required=False, )
    dateOfPublicationDistribution = forms.CharField(max_length=1000, required=True, )
    fabricatorManufacturer = forms.CharField(max_length=1000, required=False, )
    seriesStatement = forms.CharField(max_length=1000, required=False, )
    formOfCarrier = forms.CharField(max_length=1000, required=False, )
    extentOfTheCarrier = forms.CharField(max_length=1000, required=False, )
    physicalMedium = forms.CharField(max_length=1000, required=False, )
    captureMode = forms.CharField(max_length=1000, required=False, )
    dimensionsOfTheCarrier = forms.CharField(max_length=1000, required=False, )
    manifestationIdentifier = forms.CharField(max_length=1000, required=False, )
    sourceForAcquisitionAccessAuthorization = forms.CharField(max_length=1000, required=False, )
    termsOfAvailability = forms.CharField(max_length=1000, required=False, )
    accessRestrictionsOnTheManifestation = forms.CharField(max_length=1000, required=False, )
    typeface = forms.CharField(max_length=1000, required=False, )
    typeSize = forms.CharField(max_length=1000, required=False, )
    foliation = forms.CharField(max_length=1000, required=False, )
    collation = forms.CharField(max_length=1000, required=False, )
    publicationStatus = forms.CharField(max_length=1000, required=False, )
    numbering = forms.CharField(max_length=1000, required=False, )
    playingSpeed = forms.CharField(max_length=1000, required=False, )
    grooveWidth = forms.CharField(max_length=1000, required=False, )
    kindOfCutting = forms.CharField(max_length=1000, required=False, )
    tapeConfiguration = forms.CharField(max_length=1000, required=False, )
    kindOfSound = forms.CharField(max_length=1000, required=False, )
    specialReproductionCharacteristic = forms.CharField(max_length=1000, required=False, )
    colour = forms.CharField(max_length=1000, required=False, )
    reductionRatio = forms.CharField(max_length=1000, required=False, )
    polarity = forms.CharField(max_length=1000, required=False, )
    generation = forms.CharField(max_length=1000, required=False, )
    presentationFormat = forms.CharField(max_length=1000, required=False, )
    systemRequirements = forms.CharField(max_length=1000, required=False, )
    fileCharacteristics = forms.CharField(max_length=1000, required=False, )
    modeOfAccess = forms.CharField(max_length=1000, required=False, )
    accessAddress = forms.CharField(max_length=1000, required=False, )
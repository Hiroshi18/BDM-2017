# django
from django import forms

# local django
from database.models import WorkEnt


class CreateExprEntForm(forms.Form):
    identifier = forms.CharField(max_length=1000, blank=True, null=True)
    titleOfTheExpression = forms.CharField(max_length=1000, blank=True, null=True)
    formOfExpression = forms.CharField(max_length=1000, blank=True, null=True)
    dateOfExpression = forms.CharField(max_length=1000, blank=True, null=True)
    languageOfExpression = forms.CharField(max_length=1000, blank=True, null=True)
    otherDistinguishingCharacteristic = forms.CharField(max_length=1000, blank=True, null=True)
    extensibilityOfExpression = forms.CharField(max_length=1000, blank=True, null=True)
    revisabilityOfExpression = forms.CharField(max_length=1000, blank=True, null=True)
    extentOfTheExpression = forms.CharField(max_length=1000, blank=True, null=True)
    summarizationOfContent = forms.CharField(max_length=1000, blank=True, null=True)
    contextForTheExpression = forms.CharField(max_length=1000, blank=True, null=True)
    criticalResponseToTheExpression = forms.CharField(max_length=1000, blank=True, null=True)
    useRestrictionsOnTheExpression = forms.CharField(max_length=1000, blank=True, null=True)
    sequencingPattern = forms.CharField(max_length=1000, blank=True, null=True)
    expectedRegularityOfIssue = forms.CharField(max_length=1000, blank=True, null=True)
    expectedFrequencyOfIssue = forms.CharField(max_length=1000, blank=True, null=True)
    typeOfScore = forms.CharField(max_length=1000, blank=True, null=True)
    mediumOfPerformance = forms.CharField(max_length=1000, blank=True, null=True)
    scale = forms.CharField(max_length=1000, blank=True, null=True)
    projection = forms.CharField(max_length=1000, blank=True, null=True)
    presentationTechnique = forms.CharField(max_length=1000, blank=True, null=True)
    representationOfRelief = forms.CharField(max_length=1000, blank=True, null=True)
    geodeticGridAndVerticalMeasurement = forms.CharField(max_length=1000, blank=True, null=True)
    recordingTechnique = forms.CharField(max_length=1000, blank=True, null=True)
    specialCharacteristic = forms.CharField(max_length=1000, blank=True, null=True)
    technique = forms.CharField(max_length=1000, blank=True, null=True)
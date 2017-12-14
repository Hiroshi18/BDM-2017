# Django
from django import forms

# Local Django
from database.models import WorkEnt, ExprEnt


class CreateExprEntForm(forms.ModelForm):
    class Meta:
        model = ExprEnt
        exclude = ('relatedManifList',)

    identifier = forms.CharField(max_length=1000, required=False, )
    titleOfTheExpression = forms.CharField(max_length=1000, required=False, )
    formOfExpression = forms.CharField(max_length=1000, required=False, )
    dateOfExpression = forms.CharField(max_length=1000, required=True, )
    languageOfExpression = forms.CharField(max_length=1000, required=False, )
    otherDistinguishingCharacteristic = forms.CharField(max_length=1000, required=False, )
    extensibilityOfExpression = forms.CharField(max_length=1000, required=False, )
    revisabilityOfExpression = forms.CharField(max_length=1000, required=False, )
    extentOfTheExpression = forms.CharField(max_length=1000, required=False, )
    summarizationOfContent = forms.CharField(max_length=1000, required=False, )
    contextForTheExpression = forms.CharField(max_length=1000, required=False, )
    criticalResponseToTheExpression = forms.CharField(max_length=1000, required=False, )
    useRestrictionsOnTheExpression = forms.CharField(max_length=1000, required=False, )
    sequencingPattern = forms.CharField(max_length=1000, required=False, )
    expectedRegularityOfIssue = forms.CharField(max_length=1000, required=False, )
    expectedFrequencyOfIssue = forms.CharField(max_length=1000, required=False, )
    typeOfScore = forms.CharField(max_length=1000, required=False, )
    mediumOfPerformance = forms.CharField(max_length=1000, required=False, )
    scale = forms.CharField(max_length=1000, required=False, )
    projection = forms.CharField(max_length=1000, required=False, )
    presentationTechnique = forms.CharField(max_length=1000, required=False, )
    representationOfRelief = forms.CharField(max_length=1000, required=False, )
    geodeticGridAndVerticalMeasurement = forms.CharField(max_length=1000, required=False, )
    recordingTechnique = forms.CharField(max_length=1000, required=False, )
    specialCharacteristic = forms.CharField(max_length=1000, required=False, )
    technique = forms.CharField(max_length=1000, required=False, )

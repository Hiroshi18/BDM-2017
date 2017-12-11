# django
from django import forms

# local django
from database.models import WorkEnt


class CreateWorkEntForm(forms.Form):
    identifier = forms.CharField(max_length=1000, blank=True, null=True)
    titleOfTheWork = forms.CharField(max_length=1000, blank=True, null=True)
    formOfWork = forms.CharField(max_length=1000, blank=True, null=True)
    dateOfTheWork = forms.CharField(max_length=1000, blank=True, null=True)
    otherDistinguishingCharacteristic = forms.CharField(max_length=1000, blank=True, null=True)
    intendedTermination = forms.CharField(max_length=1000, blank=True, null=True)
    intendedAudience = forms.CharField(max_length=1000, blank=True, null=True)
    contextForTheWork = forms.CharField(max_length=1000, blank=True, null=True)
    mediumOfPerformance = forms.CharField(max_length=1000, blank=True, null=True)
    numericDesignation = forms.CharField(max_length=1000, blank=True, null=True)
    key = forms.CharField(max_length=1000, blank=True, null=True)
    coordinates = forms.CharField(max_length=1000, blank=True, null=True)
    equinox = forms.CharField(max_length=1000, blank=True, null=True)
    subjectOfTheWork = forms.CharField(max_length=1000, blank=True, null=True)
    placeOfOriginOfTheWork = forms.CharField(max_length=1000, blank=True, null=True)
    history = forms.CharField(max_length=1000, blank=True, null=True)
# django
from django import forms

# local django
from database.models import WorkEnt


class CreateItemEntForm(forms.Form):
    identifier = forms.CharField(max_length=1000, blank=True, null=True)
    itemIdentifier = forms.CharField(max_length=1000, blank=True, null=True)
    fingerprint = forms.CharField(max_length=1000, blank=True, null=True)
    provenanceOfTheItem = forms.CharField(max_length=1000, blank=True, null=True)
    marksInscriptions = forms.CharField(max_length=1000, blank=True, null=True)
    exhibitionHistory = forms.CharField(max_length=1000, blank=True, null=True)
    conditionOfTheItem = forms.CharField(max_length=1000, blank=True, null=True)
    treatmentHistory = forms.CharField(max_length=1000, blank=True, null=True)
    scheduledTreatment = forms.CharField(max_length=1000, blank=True, null=True)
    accessRestrictionsOnTheItem = forms.CharField(max_length=1000, blank=True, null=True)
    locationOfItem = forms.CharField(max_length=1000, blank=True, null=True)
    custodialHistoryOfItem = forms.CharField(max_length=1000, blank=True, null=True)
    immediateSourceOfAcquisitionOfItem = forms.CharField(max_length=1000, blank=True, null=True)
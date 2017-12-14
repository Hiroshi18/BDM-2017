# Django
from django import forms

# Local Django
from database.models import ManifEnt, ItemEnt


class CreateItemEntForm(forms.ModelForm):
    class Meta:
        model = ItemEnt
        fields = '__all__'

    identifier = forms.CharField(max_length=1000, required=False, )
    itemIdentifier = forms.CharField(max_length=1000, required=False, )
    fingerprint = forms.CharField(max_length=1000, required=False, )
    provenanceOfTheItem = forms.CharField(max_length=1000, required=False, )
    marksInscriptions = forms.CharField(max_length=1000, required=False, )
    exhibitionHistory = forms.CharField(max_length=1000, required=False, )
    conditionOfTheItem = forms.CharField(max_length=1000, required=False, )
    treatmentHistory = forms.CharField(max_length=1000, required=False, )
    scheduledTreatment = forms.CharField(max_length=1000, required=False, )
    accessRestrictionsOnTheItem = forms.CharField(max_length=1000, required=False, )
    locationOfItem = forms.CharField(max_length=1000, required=False, )
    custodialHistoryOfItem = forms.CharField(max_length=1000, required=False, )
    immediateSourceOfAcquisitionOfItem = forms.CharField(max_length=1000, required=False, )


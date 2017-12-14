# django
from django import forms

# local django
from database.models import WorkEnt


class CreateWorkEntForm(forms.ModelForm):
    class Meta:
        model = WorkEnt
        exclude = ('relatedExprList',)

    identifier = forms.CharField(max_length=1000, required=False, )
    titleOfTheWork = forms.CharField(max_length=1000, required=False, )
    formOfWork = forms.CharField(max_length=1000, required=False, )
    dateOfTheWork = forms.CharField(max_length=1000, required=True,)
    otherDistinguishingCharacteristic = forms.CharField(max_length=1000, required=False, )
    intendedTermination = forms.CharField(max_length=1000, required=False, )
    intendedAudience = forms.CharField(max_length=1000, required=False, )
    contextForTheWork = forms.CharField(max_length=1000, required=False, )
    mediumOfPerformance = forms.CharField(max_length=1000, required=False, )
    numericDesignation = forms.CharField(max_length=1000, required=False, )
    key = forms.CharField(max_length=1000, required=False, )
    coordinates = forms.CharField(max_length=1000, required=False, )
    equinox = forms.CharField(max_length=1000, required=False, )
    subjectOfTheWork = forms.CharField(max_length=1000, required=False, )
    placeOfOriginOfTheWork = forms.CharField(max_length=1000, required=False, )
    history = forms.CharField(max_length=1000, required=False, )
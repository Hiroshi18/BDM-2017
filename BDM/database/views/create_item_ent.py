# Django
from django.views.generic import CreateView
from django.urls import reverse
from django.http import HttpResponseRedirect

# Local Django
from database.models import ItemEnt, ManifEnt
from database.forms import CreateItemEntForm


class CreateItemEntView(CreateView):
    template_name = 'create_item_ent.html'
    sucesss_url = 'create_item_ent.html'
    form_class = CreateItemEntForm

    def get_success_url(self):
        return reverse('create_item_ent')

    def form_valid(self, form):
        identifier = form.cleaned_data['identifier']
        itemIdentifier = form.cleaned_data['itemIdentifier']
        fingerprint = form.cleaned_data['fingerprint']
        provenanceOfTheItem = form.cleaned_data['provenanceOfTheItem']
        marksInscriptions = form.cleaned_data['marksInscriptions']
        exhibitionHistory = form.cleaned_data['exhibitionHistory']
        conditionOfTheItem = form.cleaned_data['conditionOfTheItem']
        treatmentHistory = form.cleaned_data['treatmentHistory']
        scheduledTreatment = form.cleaned_data['scheduledTreatment']
        accessRestrictionsOnTheItem = form.cleaned_data['accessRestrictionsOnTheItem']
        locationOfItem = form.cleaned_data['locationOfItem']
        custodialHistoryOfItem = form.cleaned_data['custodialHistoryOfItem']
        immediateSourceOfAcquisitionOfItem = form.cleaned_data['immediateSourceOfAcquisitionOfItem']
        relatedManifEnt = form.cleaned_data['relatedManifEnt']

        item = ItemEnt()
        item.identifier = identifier
        item.itemIdentifier = itemIdentifier
        item.fingerprint = fingerprint
        item.provenanceOfTheItem = provenanceOfTheItem
        item.marksInscriptions = marksInscriptions
        item.exhibitionHistory = exhibitionHistory
        item.conditionOfTheItem = conditionOfTheItem
        item.treatmentHistory = treatmentHistory
        item.scheduledTreatment = scheduledTreatment
        item.accessRestrictionsOnTheItem = accessRestrictionsOnTheItem
        item.locationOfItem = locationOfItem
        item.custodialHistoryOfItem = custodialHistoryOfItem
        item.immediateSourceOfAcquisitionOfItem = immediateSourceOfAcquisitionOfItem
        item.relatedManifEnt = relatedManifEnt
        item.save()

        manif = ManifEnt.objects.get(pk=item.relatedManifEnt.pk)
        manif.relatedItemList.add(item)

        return HttpResponseRedirect(reverse('create_item_ent'))

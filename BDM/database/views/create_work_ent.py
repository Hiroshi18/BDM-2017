# Django
from django.views.generic import CreateView
from django.urls import reverse
from django.http import HttpResponseRedirect

# Local Django
from database.models import WorkEnt
from database.forms import CreateWorkEntForm


class CreateWorkEntView(CreateView):
    template_name = 'create_work_ent.html'
    sucesss_url = 'create_work_ent.html'
    form_class = CreateWorkEntForm
    model = WorkEnt

    def get_success_url(self):
        return reverse('create_work_ent')

    def form_valid(self, form):
        identifier = form.cleaned_data['identifier']
        titleOfTheWork = form.cleaned_data['titleOfTheWork']
        formOfWork = form.cleaned_data['formOfWork']
        dateOfTheWork = form.cleaned_data['dateOfTheWork']
        otherDistinguishingCharacteristic = form.cleaned_data['otherDistinguishingCharacteristic']
        intendedTermination = form.cleaned_data['intendedTermination']
        intendedAudience = form.cleaned_data['intendedAudience']
        contextForTheWork = form.cleaned_data['contextForTheWork']
        mediumOfPerformance = form.cleaned_data['mediumOfPerformance']
        numericDesignation = form.cleaned_data['numericDesignation']
        key = form.cleaned_data['key']
        coordinates = form.cleaned_data['coordinates']
        equinox = form.cleaned_data['equinox']
        subjectOfTheWork = form.cleaned_data['subjectOfTheWork']
        placeOfOriginOfTheWork = form.cleaned_data['placeOfOriginOfTheWork']
        history = form.cleaned_data['history']

        work = WorkEnt()
        work.identifier = identifier
        work.titleOfTheWork = titleOfTheWork
        work.formOfWork = formOfWork
        work.dateOfTheWork = dateOfTheWork
        work.otherDistinguishingCharacteristic = otherDistinguishingCharacteristic
        work.intendedTermination = intendedTermination
        work.intendedAudience = intendedAudience
        work.contextForTheWork = contextForTheWork
        work.mediumOfPerformance = mediumOfPerformance
        work.numericDesignation = numericDesignation
        work.key = key
        work.coordinates = coordinates
        work.equinox = equinox
        work.subjectOfTheWork = subjectOfTheWork
        work.placeOfOriginOfTheWork = placeOfOriginOfTheWork
        work.history = history
        work.save()

        return HttpResponseRedirect(reverse('create_work_ent'))

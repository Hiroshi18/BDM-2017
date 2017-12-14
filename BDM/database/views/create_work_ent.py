# Django
from django.views.generic import CreateView
from django.urls import reverse

# Local Django
from database.models import WorkEnt


class CreateWorkEntView(CreateView):
    template_name = 'create_work_ent.html'
    sucesss_url = 'create_work_ent.html'
    model = WorkEnt
    fields = (
                'identifier',
                'titleOfTheWork',
                'formOfWork',
                'dateOfTheWork',
                'otherDistinguishingCharacteristic',
                'intendedTermination',
                'intendedAudience',
                'contextForTheWork',
                'mediumOfPerformance',
                'numericDesignation',
                'key',
                'coordinates',
                'equinox',
                'subjectOfTheWork',
                'placeOfOriginOfTheWork',
                'history',
            )

    def get_success_url(self):
        return reverse('create_work_ent')
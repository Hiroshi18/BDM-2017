# Django
from django.views.generic import CreateView
from django.urls import reverse

# Local Django
from database.models import ManifEnt


class CreateManifEntView(CreateView):
    template_name = 'create_manif_ent.html'
    sucesss_url = 'create_manif_ent.html'
    model = ManifEnt
    fields = '__all__'

    def get_success_url(self):
        return reverse('create_manif_ent')
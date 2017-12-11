# Django
from django.views.generic import CreateView
from django.urls import reverse

# Local Django
from database.models import ItemEnt


class CreateItemEntView(CreateView):
    template_name = 'create_item_ent.html'
    sucesss_url = 'create_item_ent.html'
    model = ItemEnt
    fields = '__all__'

    def get_success_url(self):
        return reverse('create_item_ent')
# Django imports
from django.views.generic import ListView

# Local Django imports
from database.models import ItemEnt


class ListItemEntView(ListView):

    template_name = 'list_item_ent.html'
    context_object_name = 'list_item_ent'
    model = ItemEnt
    paginate_by = 20

    def dispatch(self, *args, **kwargs):
        return super(ListItemEntView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return self.model.objects.all()

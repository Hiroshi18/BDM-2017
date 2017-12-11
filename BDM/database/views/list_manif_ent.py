# Django imports
from django.views.generic import ListView

# Local Django imports
from database.models import ManifEnt


class ListManifEntView(ListView):

    template_name = 'list_manif_ent.html'
    context_object_name = 'list_manif_ent'
    model = ManifEnt
    paginate_by = 20

    def dispatch(self, *args, **kwargs):
        return super(ListManifEntView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return self.model.objects.all()

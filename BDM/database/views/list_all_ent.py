# Django imports
from django.views.generic import ListView

# Local Django imports
from database.models import WorkEnt


class ListAllEntView(ListView):
    template_name = 'list_all_ent.html'
    context_object_name = 'list_all_ent'
    model = WorkEnt
    paginate_by = 20

    def dispatch(self, *args, **kwargs):
        return super(ListAllEntView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return self.model.objects.all()

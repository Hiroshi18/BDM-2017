# Django imports
from django.views.generic import ListView

# Local Django imports
from database.models import WorkEnt


class ListWorkEntView(ListView):
    template_name = 'list_work_ent.html'
    context_object_name = 'list_work_ent'
    model = WorkEnt
    paginate_by = 20

    def dispatch(self, *args, **kwargs):
        return super(ListWorkEntView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return self.model.objects.all()

# Django
from django.views.generic import ListView
from django.urls import reverse

# Local Django
from database.models import WorkEnt


class SearchWorkEntView(ListView):
    template_name = 'list_work_ent.html'
    context_object_name = 'list_work_ent'
    model = WorkEnt
    paginate_by = 20

    def dispatch(self, *args, **kwargs):
        return super(SearchWorkEntView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        if len(self.args) > 0:
            return self.model.objects.filter(titleOfTheWork__icontains=self.args[0])
        else:
            return self.model.objects.filter()
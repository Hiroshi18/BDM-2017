# Django
from django.views.generic import CreateView
from django.urls import reverse
# Local Django
from database.forms import CreateWorkEntForm


class CreateWorkEntView(CreateView):
    template_name = 'create_work.html'
    sucesss_url = 'create_work.html'
    form_class = CreateWorkEntForm

    def dispatch(self, *args, **kwargs):
        return super(CreateWorkEntView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('list_all_medicines')

    def form_valid(self, form):
        return super().form_valid(form)

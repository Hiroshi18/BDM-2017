# Django
from django.views.generic import CreateView
from django.urls import reverse

# Local Django
from database.models import ExprEnt


class CreateExprEntView(CreateView):
    template_name = 'create_expr_ent.html'
    sucesss_url = 'create_expr_ent.html'
    model = ExprEnt
    fields = '__all__'

    def get_success_url(self):
        return reverse('create_expr_ent')
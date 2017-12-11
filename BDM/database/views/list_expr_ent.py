# Django imports
from django.views.generic import ListView

# Local Django imports
from database.models import ExprEnt


class ListExprEntView(ListView):
    template_name = 'list_expr__ent.html'
    context_object_name = 'list_expr__ent'
    model = ExprEnt
    paginate_by = 20

    def dispatch(self, *args, **kwargs):
        return super(ListExprEntView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return self.model.objects.all()

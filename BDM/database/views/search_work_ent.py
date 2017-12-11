# Django

# Local Django
from database.views import ListWorkEntView


class SearchWorkEntView(ListWorkEntView):

    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            if len(query) > 0:
                return self.model.objects.filter(titleOfTheWork__icontains=query)
            else:
                return self.model.objects.filter()

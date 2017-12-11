# Django

# Local Django
from database.views import ListWorkEntView


class SearchWorkEntView(ListWorkEntView):
    """
    Display a Blog List page filtered by the search query.
    """
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            if len(query) > 0:
                return self.model.objects.filter(titleOfTheWork__icontains=query)
            else:
                return self.model.objects.filter()

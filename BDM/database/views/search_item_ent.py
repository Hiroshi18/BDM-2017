# Django

# Local Django
from database.views import ListItemEntView


class SearchItemEntView(ListItemEntView):

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            if len(query) > 0:
                return self.model.objects.filter(identifier__icontains=query)
            else:
                return self.model.objects.filter()

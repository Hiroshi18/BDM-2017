# Django

# Local Django
from database.views import ListManifEntView


class SearchManifEntView(ListManifEntView):

    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            if len(query) > 0:
                return self.model.objects.filter(titleOfTheManifestation__icontains=query)
            else:
                return self.model.objects.filter()

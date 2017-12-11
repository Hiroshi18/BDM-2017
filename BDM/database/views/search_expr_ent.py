# Django

# Local Django
from database.views import ListExprEntView


class SearchExprEntView(ListExprEntView):

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            if len(query) > 0:
                return self.model.objects.filter(titleOfTheExpression__icontains=query)
            else:
                return self.model.objects.filter()

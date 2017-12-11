# Django
from django.conf.urls import url

# Local Django

from .views import (CreateWorkEntView,
                    CreateExprEntView,
                    CreateManifEntView,
                    CreateItemEntView,
                   )


urlpatterns = (
    url(r'^create_work_ent/$', CreateWorkEntView.as_view(), name='create_work_ent'),
    url(r'^create_expr_ent/$', CreateExprEntView.as_view(), name='create_expr_ent'),
    url(r'^create_manif_ent/$', CreateManifEntView.as_view(), name='create_manif_ent'),
    url(r'^create_item_ent/$', CreateItemEntView.as_view(), name='create_item_ent'),
)

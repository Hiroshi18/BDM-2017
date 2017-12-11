# Django
from django.conf.urls import url

# Local Django

from .views import (CreateWorkEntView,
                    CreateExprEntView,
                    CreateManifEntView,
                    CreateItemEntView,
                    ListWorkEntView,
                    ListExprEntView,
                    ListManifEntView,
                    ListItemEntView,
                    SearchWorkEntView,
                    SearchExprEntView,
                    SearchManifEntView,
                    SearchItemEntView,
                   )


urlpatterns = (
    url(r'^create_work_ent/$', CreateWorkEntView.as_view(), name='create_work_ent'),
    url(r'^list_work_ent/$', ListWorkEntView.as_view(), name='list_work_ent'),
    url(r'^search_work_ent/$', SearchWorkEntView.as_view(), name='search_work_ent'),

    url(r'^create_expr_ent/$', CreateExprEntView.as_view(), name='create_expr_ent'),
    url(r'^list_expr_ent/$', ListExprEntView.as_view(), name='list_expr_ent'),
    url(r'^search_expr_ent/$', SearchWorkEntView.as_view(), name='search_expr_ent'),

    url(r'^create_manif_ent/$', CreateManifEntView.as_view(), name='create_manif_ent'),
    url(r'^list_manif_ent/$', ListManifEntView.as_view(), name='list_manif_ent'),
    url(r'^search_manif_ent/$', SearchWorkEntView.as_view(), name='search_manif_ent'),

    url(r'^create_item_ent/$', CreateItemEntView.as_view(), name='create_item_ent'),
    url(r'^list_item_ent/$', ListItemEntView.as_view(), name='list_item_ent'),
    url(r'^search_item_ent/$', SearchWorkEntView.as_view(), name='search_item_ent'),

)

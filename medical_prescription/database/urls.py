# Django
from django.conf.urls import url

# Local Django

from .views import (CreateWorkEntView,)


urlpatterns = (
    url(r'^create_work_ent/$', CreateWorkEntView.as_view(), name='create_work_ent'),

)

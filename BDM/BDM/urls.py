from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve
from django.contrib.auth.decorators import login_required

from landing.views import home, team_page
from BDM import settings

from django.template.response import TemplateResponse


@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)


urlpatterns = [
    url(r'^user/', include('user.urls')),
    url(r'^medicine/', include('medicine.urls')),
    url(r'^exam/', include('exam.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='landing_page'),
    url(r'^team/', team_page, name='team_page'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^chat/', include('chat.urls')),
    url(r'^recommendation/', include('recommendation.urls')),
    url(r'^database/', include('database.urls')),
    url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], protected_serve, {'document_root': settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += i18n_patterns(
    url(r'^user/', include('user.urls')),
    url(r'^medicine/', include('medicine.urls')),
    url(r'^exam/', include('exam.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='landing_page'),
    url(r'^team/', team_page, name='team_page'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^chat/', include('chat.urls')),
    url(r'^recommendation/', include('recommendation.urls')),
    url(r'^database/', include('database.urls')),
)

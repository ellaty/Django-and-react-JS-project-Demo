from django.conf.urls import url
from LogsApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^log$',views.LogsApi),
    url(r'^logBySeverity/([0-9]+)$',views.LogsApiSearchBySeverity),
    url(r'^logByProducer/([a-z]*)$',views.LogsApiSearchByProducer),
    url(r'^logByDate/(?P<startDate>\d{4}-\d{2}-\d{2}.*)/(?P<endDate>\d{4}-\d{2}-\d{2}.*)$',views.LogsSearchByDate)

    ]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
from django.conf.urls import include, url
from django.contrib import admin

from integration.views import *

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^display/(?P<id>[1-9])$', display, name='display'),

	url(r'^dataset_selection$', dataset_selection, name='dataset_selection'),
	url(r'^dataset_configuration$', dataset_config, name='dataset_config'),
	url(r'^algorithm_selection$', algorithm_selection, name='algo_select'),
	url(r'^algorithm_configuration$', algorithm_config, name='algo_config'),
	url(r'^algorithm_execution/(?P<id>[1-9])$', execute_algo, name='exe_algo'),
]
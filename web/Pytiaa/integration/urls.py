from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'integration.views.index', name='index'),
	url(r'^run$', 'integration.views.run'),
	url(r'^display/(?P<id>[1-9])$', 'integration.views.display', name='display'),

	url(r'^dataset_selection$', 'integration.views.dataset_selection', name='dataset_selection'),
	url(r'^dataset_configuration$', 'integration.views.dataset_config', name='dataset_config'),
	url(r'^algorithm_selection$', 'integration.views.algorithm_selection', name='algo_select'),
	url(r'^algorithm_configuration$', 'integration.views.algorithm_config', name='algo_config'),
	url(r'^algorithm_execution$', 'integration.views.execute_algo', name='exe_algo'),
]

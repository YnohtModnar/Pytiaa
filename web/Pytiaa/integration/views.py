from django.shortcuts import render, redirect

from integration.forms import *
from integration.algorithms.kmeans import *
from integration.algorithms.PairBased import *
from integration.algorithms.Fadana import *
# from integration.algorithms.SimpleAnalogical import *
from integration.algorithms.dataset import *
from integration.algorithms.preview import *

from random import uniform

# import pdb; pdb.set_trace()

# Create your views here.
def index(request):
	return redirect('dataset_selection')

def display(request, id):
	if(request.method == 'POST'):
		if(request.POST.get('next') is not None):
			id = int(id) + 1
		else:
			id = int(id) - 1
	return render(request, 'integration/success.html', locals())

def dataset_config(request):
	has_preview = False
	name = request.session.get('typeDataset')

	if(request.method == 'POST'):
		form = _get_dataset_form(request.session.get('typeDataset'), request.POST)
		a = request.session.get('typeDataset')
		if(form.is_valid()):
			if(name == 'random'):
				request.session['dataset'] = random_generation(form.cleaned_data['nbPoints'],
															   form.cleaned_data['nbClass'],)
			elif(name == 'uniformGroup'):
				request.session['dataset'] = group_generation(form.cleaned_data['nbClass'],
															  form.cleaned_data['nbPointPerClass'],)
			elif(name == 'percentGroup'):
				request.session['dataset'], loss = percent_generation(form.cleaned_data['percents'],
																	  form.cleaned_data['nbPoints'],)
			# Generate the preview of the training set
			preview(request.session['dataset'])
			has_preview = True

			# Redirect if the user wants to go to the algorithm selection
			if('nextstep' in request.POST):
				return redirect('algo_select')
	else:
		form = _get_dataset_form(request.session.get('typeDataset'))

	return render(request, 'integration/dataset_configuration.html', {'form': form, 'has_preview': has_preview})

def _get_dataset_form(name, data=None):
	if(name == 'random'):
		return RandomGenerationForm(data)
	elif(name == 'uniformGroup'):
		return UniformGroupGenerationForm(data)
	elif(name == 'percentGroup'):
		return PercentGroupGenerationForm(data)

def _get_algo_form(name, data=None):
	if(name == 'kmeans'):
		return KmeansForm(data)
	elif(name == 'fadana'):
		return FadanaForm(data)
	elif(name == 'lazy'):
		return LazyAnalogicalForm(data)
	elif(name == 'pairBased'):
		return PairBasedForm(data)

def dataset_selection(request):
	if(request.method == 'POST'):
		form = DatasetForm(request.POST)
		if(form.is_valid()):
			request.session['typeDataset'] = form.cleaned_data['dataset']
			return redirect('dataset_config')
	else:
		form = DatasetForm()

	return render(request, 'integration/dataset_selection.html', {'form': form})


def algorithm_selection(request):
	if(request.method == 'POST'):
		form = SelectAlgorithmForm(request.POST)
		if(form.is_valid()):
			request.session['algo'] = form.cleaned_data['algorithm']
			return redirect('algo_config')
	else:
		form = SelectAlgorithmForm()

	return render(request, 'integration/algorithm_selection.html', {'form': form})


def algorithm_config(request):
	if(request.method == 'POST'):
		form = _get_algo_form(request.session.get('algo'), request.POST)
		if(form.is_valid()):
			# Execution
			_execute(form, request.session.get('dataset'), request.session.get('algo'))

			return redirect('exe_algo', 1)
	else:
		form = _get_algo_form(request.session.get('algo'))

	return render(request, 'integration/algorithm_configuration.html', {'form': form})

def _execute(form, dataset, algo):
	if(algo == 'kmeans'):
		neighbors, nneighbors, cl = kmeans(form.cleaned_data['newPoint'],
									   dataset,
									   k=form.cleaned_data['k'])
		kmeans_draw(form.cleaned_data['newPoint'], dataset, neighbors, nneighbors, cl)
	elif(algo == 'pairBased'):
		classe, c, couples = PairBased(form.cleaned_data['newPoint'], dataset)
		pb_draw(form.cleaned_data['newPoint'], dataset, c, couples, classe)
	elif(algo == 'fadana'):
		classe, triplets, analogicalDiff = fadana(form.cleaned_data['newPoint'],
												  dataset,
												  k=form.cleaned_data['k'])
		f_draw(form.cleaned_data['newPoint'], dataset, triplets, analogicalDiff, classe)
	elif(algo == 'lazy'):
		pass

def execute_algo(request, id):
	if(request.method == 'POST'):

		if(request.POST.get('next') is not None):
			id = int(id) + 1
		else:
			id = int(id) - 1

	return render(request, 'integration/algorithm_execution.html', {'id': id, 'algo': request.session.get('algo')})

import logging
from django import forms

logger = logging.getLogger(__name__)

###
#	ALGORITHM FORMS
###
class SelectAlgorithmForm(forms.Form):
		ALGORITHM = (
			('kmeans', 'K-Nearset-Neighbors'),
			('fadana', 'Fadana'),
			('lazy', 'Lazy Analogical Classification'),
			('simpleAnalogical', 'Simple Analogical'),
		)
		algorithm = forms.ChoiceField(choices=ALGORITHM, label="")
		# algorithm.widget.attrs['placeholder'] = 'Algorithm'

class AlgorithmForm(forms.Form):
	newPoint = forms.CharField(label="Point a classifier", initial=".5 .5")
	newPoint.widget.attrs['placeholder'] = "Ex: 0.5 0.5"

	def clean_newPoint(self):
		coords = self.cleaned_data['newPoint'].split(' ')
		try:
			for idx, value in enumerate(coords):
				coords[idx] = float(value)
		except ValueError as e:
			raise forms.ValidationError("The new point must be a float")

		return coords

class KmeansForm(AlgorithmForm):
	k = forms.IntegerField(label="")
	k.widget.attrs['placeholder'] = "Neighbors to use for class computation"

class FadanaForm(AlgorithmForm):
	k = forms.IntegerField(label="")
	k.widget.attrs['placeholder'] = "Triplets to user for class computation"

class LazyAnalogicalForm(AlgorithmForm):
	pass

class SimpleAnalogicalForm(AlgorithmForm):
	pass

###
#	DATASET FORMS
###
class DatasetForm(forms.Form):
	DATASET = (
		('random', u'Génération aléatoire'),
		('uniformGroup', u'Génération par groupe - uniforme'),
		('percentGroup', u'Génération par groupe - proportions'),
	)
	dataset = forms.ChoiceField(choices=DATASET, label="")
	# dataset.widget.attrs['onchange'] = 'thTis.form.submit();'

class RandomGenerationForm(forms.Form):
	nbPoints = forms.IntegerField(label="", min_value=1)
	nbPoints.widget.attrs['placeholder'] = "Nombre de points"
	nbClass = forms.IntegerField(label="", min_value=1)
	nbClass.widget.attrs['placeholder'] = "Nombre de classes"
	dimension = forms.ChoiceField(label="Dimension", choices=(('2D', '2D'), ('3D', '3D')))

class UniformGroupGenerationForm(forms.Form):
	nbClass = forms.IntegerField(label="", min_value=1)
	nbClass.widget.attrs['placeholder'] = "Nombre de classes"
	nbPointPerClass = forms.IntegerField("", min_value=1)
	nbPointPerClass.widget.attrs['placeholder'] = "Nombre de points par classe"
	dimension = forms.ChoiceField(label="Dimension", choices=(('2D', '2D'), ('3D', '3D')))

class PercentGroupGenerationForm(forms.Form):
	percents = forms.CharField(label="")
	percents.widget.attrs['placeholder'] = "Repartition des point ex: 0.5 0.3 0.2"
	nbPoints = forms.IntegerField(label="", min_value=1)
	nbPoints.widget.attrs['placeholder'] = "Nombre de points"
	dimension = forms.ChoiceField(label="Dimension", choices=(('2D', '2D'), ('3D', '3D')))

	def clean_percents(self):
		percents = self.cleaned_data['percents'].split()
		try:
			percents = list(map(float, percents)) # Cast all the percents from str to float
		except ValueError:
			raise forms.ValidationError("Format incorrect")
		# Because sum is not precise
		if(sum(percents) < 1-1e-5 or sum(percents) > 1+1e+5):
			raise forms.ValidationError("La somme doit etre égale à 1")
		return percents

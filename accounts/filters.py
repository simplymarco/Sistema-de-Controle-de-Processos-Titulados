import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class ProcessoFilter(django_filters.FilterSet):

	class Meta:
		model = Processo
		fields = ['numeroProcesso','dataProcesso', 'status']

class TerraFilter(django_filters.FilterSet):

	class Meta:
		model = Terra
		fields = ['municipio','loteamento', 'numero']

class InteressadoFilter(django_filters.FilterSet):
	nome = CharFilter(field_name='nome', lookup_expr='icontains')
	cpf = CharFilter(field_name='cpf', lookup_expr='icontains')

	class Meta:
		model = Interessado
		fields = ['nome','cpf']


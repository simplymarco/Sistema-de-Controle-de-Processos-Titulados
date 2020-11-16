from django.forms import ModelForm
from .models import Processo, Terra, Interessado, Setor

class ProcessoForm(ModelForm):
    class Meta:
        model = Processo
        fields = '__all__'

class TerraForm(ModelForm):
    class Meta:
        model = Terra
        fields = '__all__'

class InteressadoForm(ModelForm):
    class Meta:
        model = Interessado
        fields = '__all__'

class SetorForm(ModelForm):
    class Meta:
        model = Setor
        fields = '__all__'
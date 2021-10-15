from django import forms
from ..models import Diarista


class DiaristaForm(forms.ModelForm):
    #aplicando mascara nos campos necessários

    cpf = forms.CharField(widget=forms.TextInput(attrs={'data-mask': "000.000.000-00"}))
    cep = forms.CharField(widget=forms.TextInput(attrs={'data-mask': "00000-000"}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'data-mask': "(00) 00000-0000"}))

#recebe o modelo e os campos que vão fazer parte do fomulário
    class Meta:
        model = Diarista
        exclude= ('codigo_ibge',)
    #limpar mascara dos fields
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        #replace função do django que troca e limpa caracteres
        return cpf.replace('.','').replace('-','')

    def clean_cep(self):
        cep = self.cleaned_data['cep']
        return cep.replace('-', '')

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        return telefone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')


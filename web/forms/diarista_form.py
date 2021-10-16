import json
from django import forms
from ..models import Diarista
from ..services import cep_service


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
        cep_formatado = cep.replace('-', '')
        response = cep_service.buscar_cidade_cep(cep_formatado)
        if response.status_code == 400:
            raise forms.ValidationError("Cep informado é inválido")
        cidade_api =json.loads(response.content)
        if 'erro' in cidade_api:
            raise forms.ValidationError("Cep informado não encontrado")

        return cep.replace('-', '')

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        return telefone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')

    def save(self, commit=True):
        instance = super(DiaristaForm, self).save(commit=False)
        response = cep_service.buscar_cidade_cep(self.cleaned_data.get('cep'))
        cidade_api = json.loads(response.content)
        instance.codigo_ibge = cidade_api['ibge']
        instance.save()
        return instance


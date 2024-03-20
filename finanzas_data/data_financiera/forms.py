from django import forms
import datetime
from django.forms import ModelForm
from .models import Pais,Cliente,Division,Ingreso,Costo,Gasto_Operacional


class NuevoCosto(forms.ModelForm):
    MESES_CHOICES = [
        ('enero', 'Enero'),
        ('febrero', 'Febrero'),
        ('marzo', 'Marzo'),
        ('abril', 'Abril'),
        ('mayo', 'Mayo'),
        ('junio', 'Junio'),
        ('julio', 'Julio'),
        ('agosto', 'Agosto'),
        ('septiembre', 'Septiembre'),
        ('octubre', 'Octubre'),
        ('noviembre', 'Noviembre'),
        ('diciembre', 'Diciembre'),
    ]

    costo_pais = forms.ModelChoiceField(queryset=Pais.objects.all(), required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    costo_division = forms.ModelChoiceField(queryset=Division.objects.all(), required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    costo_cliente = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    costo_mes = forms.ChoiceField(choices=MESES_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    costo_anno = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    costo_real = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    costo_forecast = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    costo_ceco = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Costo
        fields = ['costo_division','costo_pais','costo_mes','costo_anno','costo_cliente','costo_ceco','costo_forecast','costo_real']

    def __init__(self, *args, **kwargs):
        super(NuevoCosto, self).__init__(*args, **kwargs)
        now = datetime.datetime.now()
        year = now.year
        ANNO_CHOICES = [(str(year - 1 + i), str(year - 1 + i)) for i in range(4)]
        self.fields['costo_anno'].choices = ANNO_CHOICES

    def save(self, commit=True):
        costo = super(NuevoCosto, self).save(commit=False)
        if commit:
            costo.save()
        return costo

    def clean_costo_real(self):
        costo_real = self.cleaned_data['costo_real']
        # Realizar cualquier manipulación o validación necesaria en ingreso_real
        return costo_real
    
    def clean_costo_forecast(self):
        costo_forecast = self.cleaned_data['costo_forecast']
        # Realizar cualquier manipulación o validación necesaria en ingreso_forecast
        return costo_forecast

    def clean_costo_pais(self):
        costo_pais = self.cleaned_data['costo_pais']
        # Realizar cualquier manipulación o validación necesaria en ingreso_pais
        return costo_pais
    
    def clean_costo_division(self):
        costo_division = self.cleaned_data['costo_division']
        # Realizar cualquier manipulación o validación necesaria en ingreso_division
        return costo_division

    def clean_costo_cliente(self):
        costo_cliente = self.cleaned_data['costo_cliente']
        # Realizar cualquier manipulación o validación necesaria en ingreso_cliente
        return costo_cliente

    def clean_costo_mes(self):
        costo_mes = self.cleaned_data['costo_mes']
        # Realizar cualquier manipulación o validación necesaria en ingreso_mes
        return costo_mes

    def clean_costo_anno(self):
        costo_anno = self.cleaned_data['costo_anno']
        # Realizar cualquier manipulación o validación necesaria en ingreso_anno
        return costo_anno

    def clean_costo_ceco(self):
        costo_ceco = self.cleaned_data['costo_ceco']
        # Realizar cualquier manipulación o validación necesaria en ingreso_ceco
        return costo_ceco

class NuevoGastoOperacional(forms.ModelForm):
    MESES_CHOICES = [
        ('enero', 'Enero'),
        ('febrero', 'Febrero'),
        ('marzo', 'Marzo'),
        ('abril', 'Abril'),
        ('mayo', 'Mayo'),
        ('junio', 'Junio'),
        ('julio', 'Julio'),
        ('agosto', 'Agosto'),
        ('septiembre', 'Septiembre'),
        ('octubre', 'Octubre'),
        ('noviembre', 'Noviembre'),
        ('diciembre', 'Diciembre'),
    ]

    gas_op_pais = forms.ModelChoiceField(queryset=Pais.objects.all(), required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gas_op_division = forms.ModelChoiceField(queryset=Division.objects.all(), required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gas_op_cliente = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gas_op_mes = forms.ChoiceField(choices=MESES_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    gas_op_anno = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    gas_op_real = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    gas_op_forecast = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    gas_op_ceco = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Gasto_Operacional
        fields = ['gas_op_division','gas_op_pais','gas_op_mes','gas_op_anno','gas_op_cliente','gas_op_ceco','gas_op_forecast','gas_op_real']

    def __init__(self, *args, **kwargs):
        super(NuevoGastoOperacional, self).__init__(*args, **kwargs)
        now = datetime.datetime.now()
        year = now.year
        ANNO_CHOICES = [(str(year - 1 + i), str(year - 1 + i)) for i in range(4)]
        self.fields['gas_op_anno'].choices = ANNO_CHOICES

    def save(self, commit=True):
        gas_op = super(NuevoGastoOperacional, self).save(commit=False)
        if commit:
            gas_op.save()
        return gas_op

    def clean_gas_op_real(self):
        gas_op_real = self.cleaned_data['gas_op_real']
        # Realizar cualquier manipulación o validación necesaria en ingreso_real
        return gas_op_real
    
    def clean_gas_op_forecast(self):
        gas_op_forecast = self.cleaned_data['gas_op_forecast']
        # Realizar cualquier manipulación o validación necesaria en ingreso_forecast
        return gas_op_forecast

    def clean_gas_op_pais(self):
        gas_op_pais = self.cleaned_data['gas_op_pais']
        # Realizar cualquier manipulación o validación necesaria en ingreso_pais
        return gas_op_pais
    
    def clean_gas_op_division(self):
        gas_op_division = self.cleaned_data['gas_op_division']
        # Realizar cualquier manipulación o validación necesaria en ingreso_division
        return gas_op_division

    def clean_gas_op_cliente(self):
        gas_op_cliente = self.cleaned_data['gas_op_cliente']
        # Realizar cualquier manipulación o validación necesaria en ingreso_cliente
        return gas_op_cliente

    def clean_gas_op_mes(self):
        gas_op_mes = self.cleaned_data['gas_op_mes']
        # Realizar cualquier manipulación o validación necesaria en ingreso_mes
        return gas_op_mes

    def clean_gas_op_anno(self):
        gas_op_anno = self.cleaned_data['gas_op_anno']
        # Realizar cualquier manipulación o validación necesaria en ingreso_anno
        return gas_op_anno

    def clean_gas_op_ceco(self):
        gas_op_ceco = self.cleaned_data['gas_op_ceco']
        # Realizar cualquier manipulación o validación necesaria en ingreso_ceco
        return gas_op_ceco

class NuevoIngreso(forms.ModelForm):

    ingreso_pais = forms.ModelChoiceField(queryset=Pais.objects.all(), required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ingreso_division = forms.ModelChoiceField(queryset=Division.objects.all(), required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ingreso_cliente = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ingreso_mes = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    ingreso_anno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    ingreso_real = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    ingreso_forecast = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    ingreso_ceco = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Ingreso
        fields = ['ingreso_division', 'ingreso_pais', 'ingreso_mes', 'ingreso_anno', 'ingreso_cliente', 'ingreso_ceco', 'ingreso_forecast', 'ingreso_real']

    # def __init__(self, *args, **kwargs):
    #     super(NuevoIngreso, self).__init__(*args, **kwargs)
    #     now = datetime.datetime.now()
    #     year = now.year
    #     ANNO_CHOICES = [(str(year - 1 + i), str(year - 1 + i)) for i in range(4)]
    #     self.fields['ingreso_anno'].choices = ANNO_CHOICES

    def save(self, commit=True):
        ingreso = super(NuevoIngreso, self).save(commit=False)
        if commit:
            ingreso.save()
        return ingreso

    def clean_ingreso_real(self):
        ingreso_real = self.cleaned_data['ingreso_real']
        # Realizar cualquier manipulación o validación necesaria en ingreso_real
        return ingreso_real
    
    def clean_ingreso_forecast(self):
        ingreso_forecast = self.cleaned_data['ingreso_forecast']
        # Realizar cualquier manipulación o validación necesaria en ingreso_forecast
        return ingreso_forecast

    def clean_ingreso_pais(self):
        ingreso_pais = self.cleaned_data['ingreso_pais']
        # Realizar cualquier manipulación o validación necesaria en ingreso_pais
        return ingreso_pais
    
    def clean_ingreso_division(self):
        ingreso_division = self.cleaned_data['ingreso_division']
        # Realizar cualquier manipulación o validación necesaria en ingreso_division
        return ingreso_division

    def clean_ingreso_cliente(self):
        ingreso_cliente = self.cleaned_data['ingreso_cliente']
        # Realizar cualquier manipulación o validación necesaria en ingreso_cliente
        return ingreso_cliente

    def clean_ingreso_mes(self):
        ingreso_mes = self.cleaned_data['ingreso_mes']
        # Realizar cualquier manipulación o validación necesaria en ingreso_mes
        return ingreso_mes

    def clean_ingreso_anno(self):
        ingreso_anno = self.cleaned_data['ingreso_anno']
        # Realizar cualquier manipulación o validación necesaria en ingreso_anno
        return ingreso_anno

    def clean_ingreso_ceco(self):
        ingreso_ceco = self.cleaned_data['ingreso_ceco']
        # Realizar cualquier manipulación o validación necesaria en ingreso_ceco
        return ingreso_ceco
    

class NuevoCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cliente_nombre', 'cliente_pais', 'cliente_division', 'cliente_ceco']
        widgets = {
            'cliente_nombre': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del cliente'}),
            'cliente_pais': forms.Select(attrs={'placeholder': 'Seleccione el país'}),
            'cliente_division': forms.Select(attrs={'placeholder': 'Seleccione la división'}),
            'cliente_ceco': forms.TextInput(attrs={'placeholder': 'Ingrese el ceco'}),
        }

class EditarIngreso(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = ['ingreso_real','ingreso_forecast']   

class EditarCosto(forms.ModelForm):
    class Meta:
        model = Costo
        fields = ['costo_real','costo_forecast']      


class EditarGastoOperacionales(forms.ModelForm):
    class Meta:
        model = Gasto_Operacional
        fields = ['gas_op_real','gas_op_forecast']      
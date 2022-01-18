from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Reset
from crispy_forms.bootstrap import FormActions
from .models import Empresa, Contacto



class EmpresaNuevaForm(forms.Form):
    denominacion=forms.CharField(
        label='Denominación social',
        widget=forms.TextInput(attrs={'placeholder': 'Denominación social/Apellidos y nombre'})
        )
    n_comercial=forms.CharField(label='Nombre comercial', required=False)
    calle=forms.CharField(
        label='Dirección'
        )
    calle2=forms.CharField(
        label= 'Dirección 2', 
        required=False
        )
    ciudad=forms.CharField()
    provincia=forms.CharField()
    cp=forms.CharField(
        label='Código Postal',
        widget=forms.TextInput(attrs={'placeholder': '00000'})
        )
    pais=forms.CharField(initial='España')
    nif=forms.CharField(
        label='NIF',
        widget=forms.TextInput(attrs={'placeholder': 'B00000000'})
        )
    email=forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email'}), 
        required=False
        )
    tfno=forms.CharField(
        label='Teléfono',
        widget=forms.TextInput(attrs={'placeholder': '+34000000000'}),
        required=False
        )
    movil=forms.CharField( required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('denominacion', css_class='form-group col-md-6 mb-0'),
                Column('n_comercial', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'calle',
            'calle2',
            Row(
                Column('ciudad', css_class='form-group col-md-4 mb-0'),
                Column('provincia', css_class='form-group col-md-4 mb-0'),
                Column('cp', css_class='form-group col-md-2 mb-0'),
                Column('pais', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('nif', css_class='form-group col-md-2 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('tfno', css_class='form-group col-md-2 mb-0'),
                Column('movil', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            FormActions(
                Submit('submit', 'Guardar'),
                Reset('Reset This Form', 'Deshacer', css_class="btn-primary"),
            )
        )




class ContactoNuevoForm(forms.Form):
    nombre = forms.CharField(label='Nombre contacto')
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.all())
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    tfno=forms.CharField(label='Teléfono',
        widget=forms.TextInput(attrs={'placeholder': '+34000000000'})
    )
    def __init__(self, *args, **kwargs):    
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'nombre',
            'empresa',
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('tfno', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            FormActions(
                Submit('submit', 'Guardar'),
                Reset('Reset This Form', 'Deshacer', css_class="btn-primary")
            )
        )

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields =[
            'nombre',
            'empresa',
            'email',
            'tfno',
        ]
    def __init__(self, *args, **kwargs):    
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'nombre',
            'empresa',
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('tfno', css_class='form-group col-md-6 mb-0'),

                css_class='form-row'
            ),
            FormActions(
                Submit('submit', 'Guardar'),
            )
        )

class EmpresaForm(forms.ModelForm):
    """Form definition for Empresa."""

    class Meta:
        """Meta definition for Empresaform."""

        model = Empresa
        fields = ('denominacion',
        'n_comercial',
        'calle',
        'calle2',
        'ciudad',
        'provincia',
        'cp',
        'pais',
        'nif',
        'email',
        'tfno',
        'movil',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('denominacion', css_class='form-group col-md-6 mb-0'),
                Column('n_comercial', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'calle',
            'calle2',
            Row(
                Column('ciudad', css_class='form-group col-md-4 mb-0'),
                Column('provincia', css_class='form-group col-md-4 mb-0'),
                Column('cp', css_class='form-group col-md-2 mb-0'),
                Column('pais', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('nif', css_class='form-group col-md-2 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('tfno', css_class='form-group col-md-2 mb-0'),
                Column('movil', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            FormActions(
                Submit('submit', 'Guardar'),
                Reset('Reset This Form', 'Deshacer', css_class="btn-primary"),
            )
        )


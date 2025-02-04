from django import forms

# ----------------- Búsqueda Simple de Producto ----------------- #
class BusquedaProductoForm(forms.Form):
    textoBusqueda = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar producto'})
    )


# ----------------- Búsqueda Avanzada de Producto ----------------- #
class BusquedaAvanzadaProductoForm(forms.Form):
    nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'})
    )
    
    tipo = forms.ChoiceField(
        choices=[('vino', 'Vino'), ('cerveza', 'Cerveza'), ('tabaco', 'Tabaco')],
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    precio_min = forms.DecimalField(
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio mínimo'})
    )

    precio_max = forms.DecimalField(
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio máximo'})
    )


# ----------------- Búsqueda Avanzada de Órdenes ----------------- #
class BusquedaAvanzadaOrdenForm(forms.Form):
    usuario = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'})
    )

    estado = forms.ChoiceField(
        choices=[('', 'Todos los estados'), ('completada', 'Completada'), ('pendiente', 'Pendiente'), ('cancelada', 'Cancelada')],
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    total_min = forms.DecimalField(
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total mínimo'})
    )

    total_max = forms.DecimalField(
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total máximo'})
    )


# ----------------- Búsqueda Avanzada de Proveedores ----------------- #
class BusquedaAvanzadaProveedorForm(forms.Form):
    nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del proveedor'})
    )

    contacto = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de contacto'})
    )

    telefono = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'})
    )

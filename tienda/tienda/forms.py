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


class ProductoForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre del Producto",
        required=True, 
        max_length=100,
        help_text="100 caracteres como máximo"
    )

    TIPO_PRODUCTO = [
        ("", "Ninguno"),
        ("vino", "Vino"),
        ("cerveza", "Cerveza"),
        ("tabaco", "Tabaco"),
    ]

    tipo = forms.ChoiceField(
        choices=TIPO_PRODUCTO,
        required=True,
        initial="",
        label="Tipo de Producto"
    )

    precio = forms.DecimalField(
        label="Precio",
        required=True,
        min_value=0.01,
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'Ingrese el precio'})
    )

    stock = forms.IntegerField(
        label="Stock",
        required=True,
        min_value=0,
        widget=forms.NumberInput(attrs={'placeholder': 'Cantidad en stock'})
    )

    descripcion = forms.CharField(
        label="Descripción",
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Descripción opcional', 'rows': 3})
    )

class ProductoActualizarNombreForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre del Producto",
        required=True, 
        max_length=100,
        help_text="100 caracteres como máximo"
    )

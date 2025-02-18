from django import forms
from .helper import helper
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

class OrdenForm(forms.Form):
    usuario = forms.IntegerField(
        label="ID del Usuario",
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el ID del usuario'})
    )

    total = forms.DecimalField(
        label="Total",
        required=True,
        min_value=0.01,
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el total'})
    )

    ESTADO_ORDEN = [
        ("", "Ninguno"),
        ("completada", "Completada"),
        ("pendiente", "Pendiente"),
        ("cancelada", "Cancelada"),
    ]

    estado = forms.ChoiceField(
        choices=ESTADO_ORDEN,
        required=True,
        label="Estado de la Orden"
    )

    metodo_pago = forms.CharField(
        label="Método de Pago",
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el método de pago'})
    )

class OrdenActualizarEstadoForm(forms.Form):
    estado = forms.ChoiceField(
        label="Estado de la Orden",
        required=True,
        choices=[
            ("", "Ninguno"),
            ("completada", "Completada"),
            ("pendiente", "Pendiente"),
            ("cancelada", "Cancelada"),
        ],
        help_text="Seleccione un estado válido para la orden"
    )


class ProveedorForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre del Proveedor",
        required=True, 
        max_length=100,
        help_text="100 caracteres como máximo"
    )

    contacto = forms.CharField(
        label="Contacto",
        required=True,
        max_length=100,
        help_text="100 caracteres como máximo"
    )

    telefono = forms.CharField(
        label="Teléfono",
        required=True,
        max_length=15,
        help_text="Máximo 15 caracteres"
    )

    correo = forms.EmailField(
        label="Correo Electrónico",
        required=False,
        help_text="Opcional"
    )

    def __init__(self, *args, **kwargs):
        super(ProveedorForm, self).__init__(*args, **kwargs)

        productosDisponibles = helper.obtener_productos()
        self.fields["productos"] = forms.MultipleChoiceField(
            choices=productosDisponibles,
            required=True,
            help_text="Mantén pulsada la tecla control para seleccionar varios productos",
        )


class ProveedorActualizarContactoForm(forms.Form):
    contacto = forms.CharField(
        label="Contacto del Proveedor",
        required=True, 
        max_length=100,
        help_text="100 caracteres como máximo"
    )


class FavoritosForm(forms.Form):
    prioridad = forms.IntegerField(
        label="Prioridad",
        required=True,
        min_value=1,
        max_value=5,
        help_text="Elige un número entre 1 y 5"
    )
    notas = forms.CharField(
        label="Notas",
        required=False,
        max_length=200,
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Notas opcionales...'})
    )

    def __init__(self, *args, **kwargs):
        super(FavoritosForm, self).__init__(*args, **kwargs)

        # Obtén usuarios disponibles
        usuariosDisponibles = helper.obtener_usuarios()
        self.fields["usuario"] = forms.ChoiceField(
            choices=usuariosDisponibles,
            required=True,
            help_text="Selecciona un usuario"
        )

        # Obtén productos disponibles
        productosDisponibles = helper.obtener_productos()
        self.fields["producto"] = forms.ChoiceField(
            choices=productosDisponibles,
            required=True,
            help_text="Selecciona un producto"
        )

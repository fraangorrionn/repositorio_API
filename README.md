# repositorio_API
python3 -m pip install django # instalar django
python3 -m pip install django-seed # instalar seed
python3 -m pip install djangorestframework # isntalar restframework
pip install django django-environ


python3 -m venv myvenv
source myvenv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

python manage.py migrate
python manage.py makemigrations tienda
python manage.py migrate tienda
python manage.py seed tienda --number=20
python manage.py dumpdata --indent 4 > tienda/fixtures/datos.json
python manage.py loaddata tienda/fixtures/datos.json

python manage.py createsuperuser
python manage.py runserver 8001

git add . git commit -m 'Completado' git push git pull

curl -X POST "http://0.0.0.0:8000/oauth2/token/" -d "grant_type=password&username=fran&password=2004&client_id=mi_aplicacion&client_secret=mi_clave_secreta"

clave de sesion: 0v8dnhvueyq27bekllrsk6lll422yes2
Admin=2aDUr50Yu0ajtsaLdHJ9GnWmK9oTzG
Gerente=M4fomOApcodhuC9GKTjBCx4iUSOa0J
Cliente=ymPRtBBixM57xhnZKqA1bhb850e2AA

# Guía de Uso de la Aplicación

Este documento tiene como objetivo explicar, de forma clara y concisa, cómo **desplegar** la aplicación y realizar las **operaciones principales** (GET, POST, PUT, DELETE, PATCH) sobre los **productos** a través del cliente.

---

## Usuarios de Prueba

| Tipo de Usuario   | Nombre de Usuario | Contraseña |
|-------------------|-------------------|-----------|
| **Administrador** | fran              | 2004      |
| **Cliente**       | manolo            | 12Fr@n34  |
| **Gerente**       | manu              | 12Fr@n34  |

---

## 1. Requisitos Previos

- **Python 3.x**  
  Necesario para ejecutar el servidor Django.
- **Django**  
  Framework backend de la aplicación.
- **Requests** (opcional)  
  Para realizar solicitudes HTTP al backend desde scripts de Python.
- **Token de acceso válido** (si la API lo requiere)  
  Se obtiene al iniciar sesión y es necesario para las solicitudes autenticadas.

---

## 2. Desplegar la Aplicación

### 2.1 Pasos para Desplegar el Servidor Django

    1. **Clona** el repositorio en tu máquina local:
        ```bash
        git clone <URL_DE_TU_REPOSITORIO>

    2. Accede a la carpeta del proyecto
        cd <nombre_del_proyecto>

    3. Crea un entorno virtual y actívalo:
        python3 -m venv venv
        source venv/bin/activate

    4. Realiza las migraciones en la base de datos:
        pip install -r requirements.txt

    5. Inicia el servidor de desarrollo de Django:
        python manage.py migrate

    6. Inicia el servidor de desarrollo de Django:
        python manage.py runserver


La aplicación quedará disponible en http://fraangorrionn.pythonanywhere.com/

## 3. Autenticación
Antes de hacer cualquier operación, asegúrate de autenticarte si tu API requiere token. Para ello:

    1.  Envía un POST al endpoint de login:
        POST http://fraangorrionn.pythonanywhere.com/api/v1/login/

    2.  Cuerpo (JSON):
        {
            "username": "tu_usuario",
            "password": "tu_contraseña"
        }

    3.  Respuesta: Recibirás un objeto JSON con tu token de acceso, que deberás incluir en las cabeceras de las solicitudes siguientes.

## 4. Operaciones CRUD con Productos
    A continuación se muestra cómo realizar las operaciones más comunes con los productos: GET, POST, PUT, DELETE y PATCH. Si tu proyecto maneja rutas distintas, ajústalas según tu configuración.

    4.1. GET (Listar Productos)
        Objetivo: Obtener datos de la API (por ejemplo, la lista de productos).

        1.  Asegúrate de contar con un token válido (si es requerido).

        2.  Envía una solicitud GET:
            GET http://fraangorrionn.pythonanywhere.com/api/v1/productos/producto_listar_api/

        3.  Encabezados (Headers):
            Authorization: Bearer <tu_token>  # Solo si es necesario

        4.  Respuesta: El servidor devolverá un listado de productos en formato JSON.

## 4.2. POST (Crear un Producto)
    Objetivo: Crear un nuevo registro de producto.

        1.  Envía un POST al endpoint de creación:
            POST http://fraangorrionn.pythonanywhere.com/api/v1/productos/crear/

        2.  Encabezados (Headers):
            Authorization: Bearer <tu_token>
            Content-Type: application/json

        3. Cuerpo (JSON) (ejemplo):
            {
                "codigo_producto": "111111",
                "stock": 4,
                "precio": 350.00
            }

        4.  Respuesta: El servidor devolverá los detalles del producto creado.

## 4.3. PUT (Actualizar Completo un Producto)
    Objetivo: Modificar por completo un producto existente.

        1. Envía un PUT al endpoint de edición:
            PUT http://fraangorrionn.pythonanywhere.com/api/v1/productos/editar/<id_producto>/
        
        2.  Encabezados (Headers):
            Authorization: Bearer <tu_token>
            Content-Type: application/json

        3.  Cuerpo (JSON) (ejemplo):
            {
                "codigo_producto": "111111",
                "stock": 3,
                "precio": 400.00
            }

        4.  Respuesta: El servidor responderá con los datos del producto actualizado.

## 4.4. DELETE (Eliminar un Producto)
    Objetivo: Quitar un producto de la base de datos.

        1.  Envía un DELETE al endpoint correspondiente
            DELETE http://fraangorrionn.pythonanywhere.com/api/v1/productos/eliminar/<id_producto>/

        2.  Encabezados (Headers):
            Authorization: Bearer <tu_token>
            Content-Type: application/json

        3.  Cuerpo (JSON) (ejemplo):
            {
                "codigo_producto": "111111"
            }

        4.  Respuesta: Devuelve los detalles del producto tras la actualización parcial.

5. Errores que pueden pasar
    401 Unauthorized
        No estás autenticado o el token ha expirado.

    404 Not Found
        URL o recurso inexistente.
        
    400 Bad Request
        Error en los datos enviados (p. ej., formato JSON incorrecto).







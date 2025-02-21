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
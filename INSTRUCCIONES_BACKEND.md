### Para generar los modelos a partir de la base de datos en mysql
pip install sqlacodegen
sqlacodegen mysql+pymysql://retos_viajes_app:retos_viajes_app@localhost/retos_viajes_app > models.py


### Correr un microservicio
uvicorn category_controller:app --reload --port 5000

### Hacer cambios en la base de datos
alembic revision --autogenerate -m "Crear db"
alembic upgrade head

### Claves para autenticación 
- Generar en linux
    ```
    openssl rand -hex 32
    ```
### Cambio en el nombre de funciones de la api rest

borrar venv y crear de nuevo
python -m venv retos_viajes_app
pip install -r requirements.txt

### Estandares
Nombres de schemma: singular
Nombres de router: plural
Devolvemos:
- Update
```json
{"message": "mensaje"}
```
- Crear
```json
{"id": "..."}
```
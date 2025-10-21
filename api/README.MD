## API BASICA PARA GESTOR DE INVENTARIO

### Como inicializar el proyecto

- Crea un entorno virtual para la correcta ejecucion de los paquetes de python con pip, puedes generarla con venv, depende de tu OS 

el comando depende de tu version de python, este caso yo utilice la 3

```bash
cd api/
python3 -m venv venv 

# activa el entorno 
source venv/bin/activate 
```

- Instala las dependencias, asegurate que los paquetes se instalen correctamente. 

```bash
pip install -r requirements.txt 
```

- Crea la base de datos en postgres, el nombre es de tu preferencia, lo importante es referenciar en el .env el mismo nombre, no es necesario crear un usuario como invitado, referencialo con el mismo usuario base de postgres y la password que tenga.

``` bash
sudo -u postgres psql 
#psql# CREATE DATABASE inventory_db; 
```

- Configura las variables de entorno:

```txt
DATABASE_URL=...
ALGORITHM=...
SECRET_KEY=Es para identificar el token jwt 
ACCESS_TOKE_EXPIRE_MINUTES=...
```

- Correr API: Estando activado el entorno virtual y todas las dependencias instaladas 

```bash 
cd api/
uvicorn main:app --reload 
```
por defecto el puerto donde se inicializa es el :8000 

- Configura el cors en el middleware para que acepte el host con el puerto del server donde tu levantaste la parte grafica

```py
# main.py 
app.add_middleware(
    allow_origins=[''], # frontend port 
)
```

### la api esta documentada con SWAGGER en un endpoint llamado /docs 

```txt 
http://127.0.0.1:port/docs
```


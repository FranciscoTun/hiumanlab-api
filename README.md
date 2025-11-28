# Task Manager API

API backend para gestionar tareas, desarrollada con Python 3.12.11 y compatible con entornos virtuales creados con `virtualenv`. Este servicio expone endpoints para crear, leer, actualizar y eliminar tareas almacenadas en MongoDB.

## Requerimientos

* Python 3.12.11
* virtualenv
* pip 25.0.1
* MongoDB (local o remoto)

## Instalación

### 1. Crear entorno virtual

```bash
virtualenv venv
```

### Activar entorno

**Linux / MacOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

## 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Configuración

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```
PORT=<PORT>
MONGO_URI=<MONGO_CONNECTION_STRING>
MONGO_DATABASE=<DATABASE_NAME>
ALLOWED_ORIGINS=<ALLOWED_ORIGINS>
```

### Ejemplo

```
PORT=5000
MONGO_URI=mongodb://localhost:27017
MONGO_DATABASE=taskmanager
ALLOWED_ORIGINS=http://localhost:5173
```

## Ejecución

```bash
python3 start.py
```

El servidor se ejecutará en el puerto configurado en tu archivo `.env`.

## Ejercicios prácticos

Los ejercicios 1, 2 y 3 de la sección de ejercicios prácticos también se encuentran implementados en esta API y pueden ser accedidos en las siguientes rutas:

* `/tasks`
* `/products`
* `/projects`

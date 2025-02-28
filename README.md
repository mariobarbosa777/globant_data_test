# 📌 Data Engineering API - FastAPI

🚀 **Descripción**
Esta API ha sido desarrollada como parte de un challenge técnico para el rol de Data Engineer. Proporciona funcionalidades para gestionar empleados, departamentos y trabajos, realizar análisis de datos 
---

## 📑 **Tabla de Contenidos**
1. [Características Principales](#-características-principales)
2. [Tecnologías Utilizadas](#-tecnologías-utilizadas)
3. [Estructura del Proyecto](#-estructura-del-proyecto)
4. [Configuración e Instalación](#-configuración-e-instalación)
5. [Uso de la API](#-uso-de-la-api)
6. [Endpoints](#-endpoints)
7. [Autenticación (Pendiente)](#-autenticación-pendiente)
8. [Consideraciones de Seguridad](#-consideraciones-de-seguridad)
9. [Mejoras Futuras](#-mejoras-futuras)

---

## ✅ **Características Principales**
- CRUD (Create, Read) para **empleados**, **departamentos** y **trabajos**.
- Procesamiento eficiente de **batch inserts** (1-1000 registros).
- **Gestión de transacciones fallidas**, almacenando registros inválidos en tabla sql `rejected_records`.
- Endpoints de **analytics** para obtener insights clave sobre contrataciones.


---

## 🛠️ **Tecnologías Utilizadas**
- **Backend:** FastAPI
- **Base de Datos:** PostgreSQL + SQLAlchemy (async)
- **ORM:** SQLAlchemy + Pydantic
- **Seguridad:** Passlib (para hashing de contraseñas), OAuth2 JWT (pendiente)
- **Backups:** FastAVRO
- **Docker:** Contenedores para API y DB

---

## 📂 **Estructura del Proyecto**
```
📦 api
 ┣ 📂 models         # Modelos SQLAlchemy
 ┣ 📂 routers        # Endpoints de la API (CRUD, analytics, auth)
 ┣ 📂 schemas        # Esquemas de validación con Pydantic
 ┣ 📂 services       # Funciones de servicios de los endspoints 
 ┣ 📂 utils          # Funciones auxiliares (seguridad, backups, manejo de errores)
 ┣ 📜 database.py    # Configuración de la DB
 ┗ 📜 main.py        # Punto de entrada de la API
📦 db
 ┣ 📜 init.sql       # Script para crear las tablas en PostgreSQL
 ┗ 📜 insert_data.sql # Carga inicial de datos
📜 docker-compose.yml # Configuración para contenedores
📜 README.md         # Documentación del proyecto
```

---

## ⚙️ **Configuración e Instalación**
1️⃣ **Clonar el repositorio:**
```bash
git clone https://github.com/tu-usuario/data-engineering-api.git
cd data-engineering-api
```

2️⃣ **Configurar variables de entorno:**
📄 **Crear un archivo `.env`** con las siguientes variables:
```ini
DATABASE_URL=postgresql+asyncpg://user:password@db:5432/mydatabase
JWT_SECRET_KEY=supersecreto
```

3️⃣ **Levantar los contenedores con Docker:**
```bash
docker-compose up --build
```

4️⃣ **Acceder a la documentación interactiva:**
📌 Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---
## 🔐 **Autenticación (Pendiente)**
Actualmente, la API no tiene autenticación, pero está planeado el uso de **JWT con OAuth2** para proteger los endpoints.

---

## 🔒 **Consideraciones de Seguridad**
✅ Manejo seguro de contraseñas con **bcrypt**
✅ Variables de entorno para datos sensibles
✅ (Pendiente) Protección de rutas con **OAuth2 y JWT**

---

## 🚀 **Mejoras Futuras**
🔹 Implementación de **JWT** para seguridad.
🔹 Agregar **paginación** en los endpoints de `GET`.

---

📌 **Desarrollado por:** Mario Barbosa 😃


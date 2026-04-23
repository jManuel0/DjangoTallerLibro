# 📚 Gestión de Libros - Django Taller

Sistema de gestión de libros desarrollado con Django como proyecto de taller en grupo.

## 🎯 Descripción del Proyecto

Aplicación web para la gestión de una biblioteca con funcionalidades CRUD (Crear, Leer, Actualizar, Eliminar) para libros.

### Operaciones Implementadas

**Desarrollador 1 (dev-developer1):**
- ✅ **LIST** - Listar todos los libros con paginación
- ✅ **READ** - Ver detalles de un libro específico
- ✅ **CREATE** - Agregar nuevos libros
- ✅ **DELETE** - Eliminar libros

**Desarrollador 2 (dev-developer2):**
- ⏳ **UPDATE** - Editar información de libros (pendiente)

## 🛠️ Tecnologías Utilizadas

- **Python 3.13.7**
- **Django 6.0.4**
- **Bootstrap 5** - Para estilos responsivos
- **SQLite** - Base de datos por defecto

## 📋 Requisitos

- Python 3.13+
- pip (gestor de paquetes de Python)

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/jManuel0/DjangoTallerLibro.git
cd DjangoLibroTaller2
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

**En Windows (Git Bash):**
```bash
source venv/Scripts/activate
```

**En Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**En Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Aplicar migraciones

```bash
cd proyecto
python manage.py migrate
```

### 6. Crear superusuario

```bash
python manage.py createsuperuser
```

### 7. Ejecutar servidor de desarrollo

```bash
python manage.py runserver
```

## 📍 Acceso a la Aplicación

- **URL de la aplicación:** http://127.0.0.1:8000/libros/
- **Panel de administración:** http://127.0.0.1:8000/admin/

## 📁 Estructura del Proyecto

```
DjangoLibroTaller2/
├── proyecto/
│   ├── gestion/           # Aplicación Django
│   │   ├── migrations/    # Migraciones de BD
│   │   ├── templates/     # Plantillas HTML
│   │   │   └── gestion/
│   │   │       ├── base.html
│   │   │       ├── libro_list.html
│   │   │       ├── libro_detail.html
│   │   │       └── libro_confirm_delete.html
│   │   ├── admin.py       # Configuración del admin
│   │   ├── forms.py       # Formularios
│   │   ├── models.py      # Modelos de BD
│   │   ├── urls.py        # Rutas
│   │   └── views.py       # Vistas
│   ├── proyecto/          # Configuración del proyecto
│   │   ├── settings.py    # Configuración
│   │   ├── urls.py        # URLs principales
│   │   └── wsgi.py
│   ├── manage.py
│   └── db.sqlite3         # Base de datos
├── venv/                  # Entorno virtual
├── requirements.txt       # Dependencias
├── README.md             # Este archivo
└── .gitignore           # Archivos a ignorar en Git
```

## 📚 Modelo de Datos

### Libro

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | AutoField | Identificador único |
| `titulo` | CharField | Título del libro |
| `autor` | CharField | Autor del libro |
| `descripcion` | TextField | Descripción detallada |
| `fecha_publicacion` | DateField | Fecha de publicación |
| `isbn` | CharField | ISBN único del libro |
| `cantidad` | IntegerField | Cantidad disponible |
| `fecha_creacion` | DateTimeField | Fecha de creación (auto) |
| `fecha_actualizacion` | DateTimeField | Fecha de actualización (auto) |

## 🔗 Rutas Disponibles

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/libros/` | Listar todos los libros |
| GET | `/libros/<id>/` | Ver detalles de un libro |
| GET | `/libros/create/` | Mostrar formulario de creación |
| POST | `/libros/create/` | Crear nuevo libro |
| GET | `/libros/<id>/delete/` | Confirmar eliminación |
| POST | `/libros/<id>/delete/` | Eliminar libro |

## 👥 Trabajo en Equipo - Ramas Git

```
main (rama principal)
  └── dev (rama de desarrollo compartida)
      ├── dev-developer1 (Desarrollador 1) ← TÚ ESTÁS AQUÍ
      └── dev-developer2 (Desarrollador 2)
```

### Flujo de trabajo:

1. Cada desarrollador trabaja en su propia rama
2. Al completar features, hacer pull request a `dev`
3. Una vez revisado, hacer merge a `dev`
4. Finalmente, hacer merge de `dev` a `main` para release

## 🔐 Admin Panel

Accede a http://127.0.0.1:8000/admin/ con las credenciales del superusuario.

Desde aquí puedes:
- Listar todos los libros
- Buscar por título, autor o ISBN
- Filtrar por fecha de publicación
- Crear, editar y eliminar libros directamente

## 📝 Comandos Útiles

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver

# Ejecutar tests
python manage.py test

# Acceder a la shell de Django
python manage.py shell
```

## 🐛 Troubleshooting

**Error: ModuleNotFoundError: No module named 'django'**
```bash
pip install -r requirements.txt
```

**Error: no such table: auth_user**
```bash
cd proyecto
python manage.py migrate
```

**Error: Port 8000 already in use**
```bash
python manage.py runserver 8001
```

## 📧 Contacto

- **Desarrollador 1:** Juan Manuel
- **Repositorio:** https://github.com/jManuel0/DjangoTallerLibro

## 📄 Licencia

Este proyecto es de propósito educativo.

---

**Última actualización:** Abril 2026
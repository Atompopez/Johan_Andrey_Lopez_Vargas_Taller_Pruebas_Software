# Taller de Pruebas de Software

Este proyecto contiene un conjunto de ejercicios prácticos sobre pruebas de software utilizando Python y pytest. El proyecto incluye diferentes tipos de pruebas unitarias, de integración y de rendimiento para diversos componentes de software.

## 📋 Descripción

Este taller está diseñado para practicar y entender diferentes aspectos de las pruebas de software, incluyendo:

- Pruebas unitarias para funciones matemáticas
- Pruebas de integración con bases de datos
- Pruebas de sistemas de autenticación
- Pruebas de rendimiento
- Pruebas de casos límite (edge cases)

## 📁 Estructura del Proyecto

```
taller_pruebas_software/
├── main/
│   ├── ejercicio_1/          # Números de Armstrong
│   │   ├── armstrong.py
│   │   └── armstrongTest.py
│   ├── ejercicio_2/          # Sistema de autenticación
│   │   ├── auth.py
│   │   └── authTest.py
│   ├── ejercicio_3/          # Carrito de compras
│   │   ├── shop.py
│   │   └── shopTest.py
│   ├── ejercicio_4/          # Gestor de tareas
│   │   ├── taskmanager.py
│   │   └── taskmanagerTest.py
│   └── ejercicio_5/          # Búsqueda de tareas (rendimiento)
│       ├── taskSearch.py
│       └── taskSearchTest.py
├── requirements.txt          # Dependencias del proyecto
├── run_tests.py             # Script para ejecutar todos los tests
└── README.md                # Este archivo
```

## 🚀 Instalación

1. Clona el repositorio:
```bash
git clone <url-del-repositorio>
cd taller_pruebas_software
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

O si prefieres instalarlas manualmente:
```bash
pip install pytest>=7.0.0 sqlalchemy>=2.0.0
```

## 🧪 Ejecución de Tests

### Ejecutar todos los tests

Para ejecutar todos los tests del proyecto con un resumen detallado:

```bash
python3 run_tests.py
```

O usando pytest directamente:

```bash
python3 -m pytest main/ -v
```

### Ejecutar tests individuales

Para ejecutar los tests de un ejercicio específico:

```bash
# Ejercicio 1: Números de Armstrong
python3 -m pytest main/ejercicio_1/armstrongTest.py -v

# Ejercicio 2: Sistema de autenticación
python3 -m pytest main/ejercicio_2/authTest.py -v

# Ejercicio 3: Carrito de compras
python3 -m pytest main/ejercicio_3/shopTest.py -v

# Ejercicio 4: Gestor de tareas
python3 -m pytest main/ejercicio_4/taskmanagerTest.py -v

# Ejercicio 5: Búsqueda de tareas
python3 -m pytest main/ejercicio_5/taskSearchTest.py -v
```

## 📚 Ejercicios Incluidos

### Ejercicio 1: Números de Armstrong
Implementación y pruebas de una función que determina si un número es un número de Armstrong. Incluye pruebas para:
- Números válidos de Armstrong
- Números inválidos
- Casos límite (tipos incorrectos, números negativos)

### Ejercicio 2: Sistema de Autenticación
Sistema de autenticación usando SQLAlchemy con pruebas de integración que incluyen:
- Registro de usuarios
- Autenticación de usuarios
- Uso de base de datos en memoria para pruebas

### Ejercicio 3: Carrito de Compras
Sistema de carrito de compras con gestión de inventario. Pruebas para:
- Agregar productos al carrito
- Validación de stock
- Cálculo de totales
- Actualización de inventario

### Ejercicio 4: Gestor de Tareas
Sistema de gestión de tareas con pruebas UAT (User Acceptance Testing) que verifican:
- Creación de tareas
- Edición de tareas
- Eliminación de tareas

### Ejercicio 5: Búsqueda de Tareas (Rendimiento)
Servicio de búsqueda de tareas con pruebas de rendimiento que validan:
- Funcionalidad de búsqueda
- Tiempo de ejecución optimizado
- Manejo de grandes volúmenes de datos

## 📦 Dependencias

- **Python 3.12+**
- **pytest** (>=7.0.0): Framework de pruebas
- **sqlalchemy** (>=2.0.0): ORM para bases de datos (usado en ejercicio 2)

## ✅ Estado de los Tests

Todos los tests están configurados y pasando correctamente. El script `run_tests.py` proporciona un resumen detallado de la ejecución de todos los tests.

## 👥 Autores

Johan Andrey López Vargas

## 📝 Licencia

Este proyecto es parte de un taller académico de pruebas de software.


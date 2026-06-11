# Ironmongery Inventory & Alerts API 🦅🚀

Una API RESTful robusta y modular diseñada específicamente para la gestión de inventarios y el control inteligente de stock crítico para negocios de ferretería y tlapalería. Construida bajo una arquitectura limpia utilizando **FastAPI** para un alto rendimiento y **MySQL** como motor de base de datos relacional.

El sistema cuenta con un manejo estricto de reglas de negocio, validación automática de tipos de datos en las peticiones, prevención de inyecciones SQL mediante consultas parametrizadas, y controladores de excepciones HTTP para garantizar respuestas seguras y estandarizadas.

---

## 🛠️ Tecnologías y Dependencias

El núcleo del proyecto utiliza herramientas estándar de la industria backend en Python:

* **FastAPI [standard]** - Framework moderno de alto rendimiento para la construcción de APIs.
* **Uvicorn** - Servidor ASGI rápido para la ejecución del entorno de desarrollo.
* **MySQL Connector Python** - Controlador nativo para la comunicación optimizada con la base de datos.
* **Pydantic** - Validación estricta y tipado de esquemas de datos en tiempo de ejecución.

---

## 📂 Arquitectura del Proyecto

El código está organizado bajo una estructura modular que separa de manera estricta las rutas de acceso (endpoints) de la lógica de persistencia de datos (consultas SQL):

```text
APIR_FERRETERIA/
├── crud/
│   └── ironmongery_crud.py   # Lógica de operaciones de la base de datos (SQL)
├── databases/
│   ├── connection.py         # Módulo de conexión segura a MySQL (XAMPP)
│   └── schema.sql            # Script de inicialización de la Base de Datos
├── .gitignore                # Filtro de archivos para el control de versiones
├── main.py                   # Cerebro de la API (Rutas y Endpoints de FastAPI)
└── requirements.txt          # Lista de dependencias del proyecto

🧬 Endpoints del Servidor (Contrato de la API)
La API implementa un esquema CRUD completo junto con un sistema inteligente de monitoreo a través de los siguientes métodos HTTP estandarizados:
MétodoEndpointDescripciónValidación de Entrada / Reglas de NegocioGET/Estado del servicio (Health Check)Ninguna. Retorna estado del core.GET/ironObtiene la lista completa de herramientasNinguna. Retorna lista mapeada en diccionarios.GET/iron/alertsMódulo Inteligente: Filtra stock críticoDevuelve productos donde cantidad_actual <= stock_minimo_alerta.GET/iron/{id}Busca un producto específico por su IDParámetro de ruta (int) con filtro de existencia 404.POST/ironRegistra un nuevo producto en el inventarioValidación estricta vía IronSchema (JSON body).PUT/ironActualiza costos, precios y stockParámetros de consulta (query params) con validación de tipos y filtro 404.DELETE/iron/{iron_id}Elimina un producto permanentementeParámetro de ruta (int) con filtro de existencia 404.

git clone [https://github.com/TU_USUARIO/apir_ferreteria.git](https://github.com/TU_USUARIO/apir_ferreteria.git)
cd apir_ferreteria

2. Configurar el Entorno Virtual (Recomendado)
python -m venv .venv

Para activar el entorno virtual en Windows, ejecuta el siguiente comando según tu terminal:
# En PowerShell:
.venv\Scripts\Activate.ps1

# En la CMD clásica:
.venv\Scripts\activate.bat

3. Instalar dependencias necesarias
Con el entorno virtual activo y limpio, instala los paquetes requeridos:
pip install -r requirements.txt

4. Inicializar la Base de Datos en MySQL
Asegúrate de tener tu servidor local encendido desde el panel de XAMPP (módulos Apache y MySQL en verde).

Abre tu gestor de base de datos o ingresa a phpMyAdmin en tu navegador (http://localhost/phpmyadmin).

Importa o ejecuta el script ubicado en databases/schema.sql para crear de forma automática la base de datos ferreteria_db y la tabla productos con sus datos semilla de prueba.

5. Encender el motor de la API
Ejecuta el servidor de FastAPI en modo de desarrollo con el entorno de recarga automática activado:
fastapi dev main.py

El servidor web comenzará a correr localmente en la dirección estándar: http://127.0.0.1:8000

📖 Documentación Interactiva Autónoma
Una vez que el servidor esté encendido, puedes acceder a la interfaz de documentación interactiva autogenerada. Esta herramienta permite probar cada uno de los endpoints en tiempo real con la base de datos de XAMPP viva, sin necesidad de usar clientes externos como Postman o Insomnia:

Swagger UI (Documentación interactiva): http://127.0.0.1:8000/docs

Desarrollado con dedicación por Alexis Gerardo Ramirez Gallardo.
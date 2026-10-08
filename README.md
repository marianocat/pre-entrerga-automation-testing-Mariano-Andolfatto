# Curso Automation testing - Pre-Entrerga
## Propósito del proyecto
Demostrar la capacidad de automatizar flujos básicos de navegación web utilizando Selenium WebDriver y Python.<br>
Para esta tarea utilizaremos el sitio [https://saucedemo.com](https://www.saucedemo.com/) que es una aplicacion especialmente diseñada para practicas de testing.

## Tecnologías a utilizar
- Python
    - pytest
    - pytest-html
- Selenium WebDriver
- Git
- GitHub

## Estructura del proyecto:
```text
pre-entrerga-automation-testing-Mariano-Andolfatto/
├── reports/
│   └── *_reporte.html
├── tests/
│   └── test_saucedemo.py
├── utils/
│   └── utiles.py
├── conftest.py
├── pytest.ini
└── requirements.txt
```

## SetUp e Instalacion de dependencias
Antes de empezar es altamente recomendable aislar el proyecto de otros usando un entorno especifico.

```ps
python -m venv .\env
```
Luego instalar las dependencias y activar el entorno:
```ps
.\env\Scripts\python.exe -m pip install -r .\requirements.txt
.\env\Scripts\Activate.ps1
```
Si la activacion del entorno falla por la politica de control de ejecucion de scripts, ejecutar el siguiente comando para permitir la ejecucion de scripts FIRMADOS en su origen:
```ps
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

## Ejecucion de las pruebas

El archivo pytest.ini ya esta preparado para ubicar correctamente los archivos y funciones de test para su ejecucion.<br> Ademas configura la generacion de reporte en HTML por lo que solo será necesaria la invocacion de pytest.
```ps
pytest
```

Si se quieren correr partes especificas de las pruebas, se puede optar por alguno de los siguientes comandos:

```ps
pytest # Para ejecutar todas las pruebas
pytest -m login #Para pruebas relacionadas con el login
pytest -m pagproductos #Para pruebas del armado de la pagina de productos
pytest -m carrito #Para pruebas relacionadas con el carrito de compras
```

Losa rechivos de resultados apareceran en la arpeta ./reports con la fecha y hora de cada ejecucion.
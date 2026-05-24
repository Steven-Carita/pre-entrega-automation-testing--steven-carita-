# Pre-Entrega Proyecto QA Automation - by Carita Steven

## Proposito del proyecto

Este proyecto tiene como objetivo automatizar pruebas funcionales basicas sobre la pagina de prueba SauceDemo utilizando Selenium WebDriver y Pytest en Python.

Las automatizaciones desarrolladas permiten validar:

- Login de usuario
- Navegacion y verificacion del catalogo de productos
- Agregar productos al carrito
- Validacion de elementos de la interfaz

---

## Estructura del proyecto

```plaintext
Pre_entrega/
│
├── conftest.py
├── requirements.txt
├── README.md
│
├── tests/
│   └── test_saucedemo.py
│
└── utils/
    └── helpers.py 

```

## Instalacion de dependencias


### 1) Clonar el repositorio

```bash
git clone https://github.com/Steven-Carita/pre-entrega-automation-testing--steven-carita-.git
```


### 2) Ingresar a la carpeta del proyecto

```bash
cd Pre_entrega
```


### 3) Instalar dependencias

```bash
pip install -r requirements.txt
```


---


## Ejecucion de pruebas


### Ejecutar todas las pruebas

```bash
pytest tests/test_saucedemo.py -v
```

### Ejecutar una prueba especifica

```bash
pytest tests/test_saucedemo.py::test_login -v
```

### Generar reporte HTML

```bash
pytest tests/test_saucedemo.py -v --html=reporte.html
```


---


## Casos automatizados

### Login

- Validacion de acceso correcto al sistema
- Verificacion de redireccion a inventario

### Catalogo de productos

- Validacion de menu y filtros
- Validacion de carga de productos
- Verificacion del nombre del primer producto

### Carrito de compras

- Agregar producto al carrito
- Validar contador del carrito
- Verificar producto agregado

---

## Sitio utilizado para pruebas

```bash
https://www.saucedemo.com/
```



# Bank Chafa

Bank Chafa es una aplicación de consola escrita en Python que simula operaciones básicas de un banco. El usuario puede introducir un saldo inicial y luego elegir entre retirar fondos, depositar dinero o salir de la sesión. Las transacciones validan montos y muestran mensajes de éxito o error.

## Requisitos

- Python 3.8 o superior
- Librería `colorama` para colorear la salida en la terminal

## Instalación

1. Crear un entorno virtual (venv) en la raíz del proyecto:
   ```bash
   python3 -m venv venv
   ```
2. Activar el entorno virtual:
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - En Windows (PowerShell):
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
3. Instalar dependencias:
   ```bash
   pip install colorama
   ```

## Uso

Una vez configurado el entorno virtual e instalada la dependencia, ejecutar el script principal:

```bash
python main.py
```
si te dá un error, ejecuta:
```bash
python3 main.py
```

Sigue las indicaciones en pantalla para introducir el saldo inicial y seleccionar las operaciones disponibles.

### By Zerik
> Version 1.0
> Gustavo Andrés Guzmán Mejía
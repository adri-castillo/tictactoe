# Tic-Tac-Toe

Este proyecto es una aplicación de backend desarrollada con Python y Django que permite jugar al Tres en Raya desde la consola.

## Requisitos

Los requisitos mínimos para el funcionamiento básico del juego:
- **Modo 2 Jugadores:** Validación de turnos para X y O.
- **Validación de Movimientos:** Control de posiciones ocupadas y rangos válidos (0-8).
- **Lógica de Juego:** Visualización del tablero y detección de victorias o empate.

## Instalación y Configuración

Sigue estos pasos para configurar el proyecto en tu entorno local:

## Instalación y Configuración

1. **Clonar el repositorio:**
   `git clone https://github.com/adri-castillo/tictactoe.git`

2. **Configurar el entorno virtual:**
   ```bash
   # Crear entorno
   python -m venv env

   # Activar en Windows:
   env\Scripts\activate

   # Activar en Mac/Linux:
   source env/bin/activate

3. **Instalar dependencias:**
   `pip install -r requirements.txt`

4. **Preparar la Base de Datos:**
   `python manage.py migrate`

## Cómo Jugar

Con el entorno activo, inicia una partida ejecutando el siguiente comando:
```bash
   python manage.py play
```

#### Controles del juego
```text
 0 | 1 | 2 
-----------
 3 | 4 | 5 
-----------
 6 | 7 | 8 
 ```
- **0 al 8**: Selecciona la casilla para marcar movimiento.
- **q**: Cancela la partida actual.
- **Ctrl + C**: Forzar salida del proceso.


## Tests Unitarios
Para ejecutar los tests, utiliza el siguiente comando:
```bash
python manage.py test
```


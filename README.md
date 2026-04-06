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

## Control y Log de Partidas

El sistema registra automáticamente cada partida en la base de datos, incluyendo fecha de creación y finalización. Para consultar el historial y las estadísticas:

1. **Crear un superusuario:**
   ```bash
   python manage.py createsuperuser
   ```
2. **Levantar servidor:** 
    ```bash 
    python manage.py runserver
    ```
3. **Acceder al panel administrativo:**
    `http://127.0.0.1:8000/admin`

4. **Consultar logs:**
En la sección "Games" podrás visualizar la lista de partidas, el ganador y la duración de cada una.

## Interfaz API REST
El juego soporta interacción vía API REST utilizando **Django REST Framework**. Lo que permite jugar desde la terminal con `curl` o cualquier cliente HTTP.

### Endpoints Principales

| Acción | Método | URL |
| :--- | :--- | :--- |
| Listar Partidas (Logs) | GET | `/api/games/` |
| Crear Nueva Partida | POST | `/api/games/` |
| Realizar Movimiento | POST | `/api/games/<id>/move/<pos>/` |
| Cancelar Partida | POST | `/api/games/<id>/cancel/` |

#### Ejemplo de uso
- **Listar partidas:**
```bash 
   curl -X GET http://127.0.0.1:8000/api/games/
```

- **Crear nueva partida:**
```bash 
   curl -X POST http://127.0.0.1:8000/api/games/
```
Respuesta: Te dará un ID
 *`{"id": 1}`*
- **Hacer movimiento:**

```bash 
   curl -X POST http://127.0.0.1:8000/api/games/1/move/4/ 
```
Primer elemento es el ID de la partida creada, y el segundo elemento es la posición en el tablero.
- **Cancelar partida:**
```bash 
   curl -X POST http://127.0.0.1:8000/api/games/1/cancel/
```
Finalizar una partida especificando su ID.



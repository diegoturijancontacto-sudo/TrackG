# TrackG - Aplicación de Seguimiento de Ejercicios con Pesas

TrackG es una aplicación de seguimiento corporal que utiliza MediaPipe para detectar y contar repeticiones de ejercicios con mancuernas. La aplicación proporciona retroalimentación en tiempo real sobre la forma correcta del ejercicio y mide el tiempo entre repeticiones.

## Características

- **Detección de pose en tiempo real** usando MediaPipe
- **6 ejercicios diferentes** de levantamiento de pesas:
  1. **Bicep Curl** - Curl de bíceps
  2. **Shoulder Press** - Press de hombros
  3. **Lateral Raise** - Elevaciones laterales
  4. **Front Raise** - Elevaciones frontales
  5. **Hammer Curl** - Curl martillo
  6. **Tricep Extension** - Extensiones de tríceps
- **Contador de repeticiones automático**
- **Cronómetro entre repeticiones** - Mide el tiempo entre cada repetición
- **Validación de ángulos** - Detecta si el ejercicio se realiza correctamente
- **Retroalimentación visual** - Indica si la forma es correcta o incorrecta
- **Interfaz intuitiva** - Fácil de usar con controles por teclado

## Requisitos

### Para la aplicación web (GitHub Pages):
- Navegador web moderno (Chrome, Firefox, Edge, Safari)
- Cámara web
- Conexión a internet (para cargar MediaPipe)

### Para la aplicación de escritorio:
- Python 3.7 o superior
- Cámara web
- Dependencias listadas en `requirements.txt`

## Uso

### Aplicación Web en GitHub Pages (Más Fácil - Recomendada)

**¡La aplicación está disponible online sin necesidad de instalación!**

Simplemente visita: **[https://diegoturijancontacto-sudo.github.io/TrackG/](https://diegoturijancontacto-sudo.github.io/TrackG/)**

1. Abre el enlace en tu navegador
2. **Permite el acceso a la cámara** cuando el navegador lo solicite
3. **Selecciona un ejercicio** haciendo clic en los botones
4. La aplicación comenzará a rastrear tus movimientos automáticamente

### Aplicación Web Local (Desarrollo)

#### Opción 1: Sin servidor (recomendada para desarrollo)
```bash
# Simplemente abre el archivo index.html en tu navegador
# O usa un servidor HTTP simple:
python -m http.server 8000
# Luego visita: http://localhost:8000
```

#### Opción 2: Con Flask (para desarrollo del backend)

1. Clona el repositorio:
```bash
git clone https://github.com/diegoturijancontacto-sudo/TrackG.git
cd TrackG
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta el servidor web:
```bash
python app.py
```

4. Abre tu navegador web y visita:
```
http://localhost:5000
```

5. **Permite el acceso a la cámara** cuando el navegador lo solicite.

6. **Selecciona un ejercicio** haciendo clic en los botones:
   - Bicep Curl (curl de bíceps)
   - Shoulder Press (press de hombros)
   - Lateral Raise (elevaciones laterales)
   - Front Raise (elevaciones frontales)
   - Hammer Curl (curl martillo)
   - Tricep Extension (extensiones de tríceps)

7. La aplicación comenzará a rastrear tus movimientos automáticamente.

### Aplicación de Escritorio (Alternativa)

1. Ejecuta la aplicación de escritorio:
```bash
python exercise_tracker.py
```

2. La aplicación se abrirá mostrando la vista de tu cámara web con el seguimiento corporal activado.

3. **Controles del teclado**:
   - **1** - Bicep Curl (curl de bíceps)
   - **2** - Shoulder Press (press de hombros)
   - **3** - Lateral Raise (elevaciones laterales)
   - **4** - Front Raise (elevaciones frontales)
   - **5** - Hammer Curl (curl martillo)
   - **6** - Tricep Extension (extensiones de tríceps)
   - **Q** - Salir de la aplicación

## Cómo Funciona

### Detección de Ejercicios

La aplicación utiliza MediaPipe Pose para detectar 33 puntos clave del cuerpo en tiempo real. Calcula los ángulos entre articulaciones específicas para determinar:

- **Fase del ejercicio** (posición inicial vs. posición final)
- **Forma correcta** (ángulos apropiados)
- **Completitud de repeticiones** (ciclo completo de movimiento)

### Retroalimentación en Tiempo Real

La interfaz muestra:
- **Ejercicio actual** - Nombre del ejercicio que estás realizando
- **Contador de repeticiones** - Número de repeticiones completadas correctamente
- **Cronómetro** - Tiempo transcurrido desde la última repetición
- **Feedback de forma** - Mensajes que indican si estás haciendo el ejercicio correctamente
  - Verde: Forma correcta ("¡Bien!", "¡Perfecto!", "¡Excelente!")
  - Naranja: Forma en progreso o necesita ajustes

### Validación de Ángulos

Cada ejercicio tiene rangos de ángulos específicos:

- **Bicep Curl**: Brazo extendido (>160°) → Flexión completa (<40°)
- **Shoulder Press**: Codos flexionados (<90°) → Brazos extendidos (>160°)
- **Lateral Raise**: Brazos abajo (<30°) → Brazos a altura de hombros (>80°)
- **Front Raise**: Brazos abajo (<30°) → Brazos al frente (>80°)
- **Hammer Curl**: Brazo extendido (>160°) → Flexión completa (<45°)
- **Tricep Extension**: Brazo flexionado (<60°) → Extensión completa (>160°)

## Consejos de Uso

1. **Iluminación**: Asegúrate de tener buena iluminación para una mejor detección
2. **Posicionamiento**: Colócate de lado a la cámara para ejercicios laterales
3. **Distancia**: Mantén una distancia de 1.5-2 metros de la cámara para que tu cuerpo completo sea visible
4. **Movimientos controlados**: Realiza los ejercicios de forma controlada para una mejor detección
5. **Calibración**: La aplicación se ajusta automáticamente a tu rango de movimiento

## Estructura del Código

```
TrackG/
├── index.html                # Página principal (GitHub Pages)
├── app.py                    # Servidor web Flask (opcional)
├── exercise_tracker.py       # Aplicación de escritorio
├── exercise_utils.py         # Utilidades y lógica de ejercicios
├── templates/
│   └── index.html           # Plantilla HTML para Flask
├── static/
│   ├── css/
│   │   └── style.css        # Estilos de la aplicación web
│   └── js/
│       └── exercise-tracker.js  # Lógica JavaScript del cliente
├── .github/
│   └── workflows/
│       └── deploy.yml       # GitHub Actions para despliegue
├── .nojekyll                # Configuración de GitHub Pages
├── requirements.txt          # Dependencias de Python
├── test_exercise_tracker.py  # Tests unitarios
├── .gitignore               # Archivos a ignorar en Git
└── README.md                # Este archivo
```

## Despliegue en GitHub Pages

La aplicación está configurada para desplegarse automáticamente en GitHub Pages:

1. **Fork** este repositorio o clónalo en tu cuenta de GitHub
2. Ve a **Settings** → **Pages** en tu repositorio
3. En **Source**, selecciona **GitHub Actions**
4. El workflow se ejecutará automáticamente al hacer push a `main` o `master`
5. Tu aplicación estará disponible en: `https://tu-usuario.github.io/TrackG/`

La aplicación funciona completamente en el navegador sin necesidad de servidor backend, utilizando:
- MediaPipe JavaScript para la detección de pose
- HTML5 Canvas para la visualización
- APIs del navegador para el acceso a la cámara

## Tecnologías Utilizadas

### Web (GitHub Pages - Aplicación Principal)
- **MediaPipe JavaScript** - Detección de pose en el navegador
- **HTML5/CSS3/JavaScript** - Interfaz de usuario moderna
- **Canvas API** - Visualización de pose en tiempo real
- **GitHub Pages** - Hosting estático gratuito
- **GitHub Actions** - Despliegue automatizado

### Backend (Aplicación de Escritorio - Opcional)
- **MediaPipe** - Framework de ML para detección de pose
- **OpenCV** - Procesamiento de video y visualización
- **NumPy** - Cálculos matemáticos y de ángulos
- **Flask** - Framework web de Python (para desarrollo local)

## Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT.

## Autor

Diego Turijan

## Agradecimientos

- MediaPipe team por su excelente framework de detección de pose
- La comunidad de OpenCV por las herramientas de visión por computadora
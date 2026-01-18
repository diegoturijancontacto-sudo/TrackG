# TrackG - Guía de Desarrollo

## Resumen del Proyecto

TrackG es una aplicación de seguimiento corporal que utiliza MediaPipe para rastrear ejercicios con mancuernas en tiempo real. La aplicación detecta la postura del usuario, calcula ángulos de articulaciones, cuenta repeticiones automáticamente y proporciona retroalimentación sobre la forma correcta del ejercicio.

## Arquitectura del Código

### Archivos Principales

1. **exercise_tracker.py** - Aplicación principal
   - Inicializa MediaPipe Pose
   - Captura video de la cámara web
   - Dibuja la interfaz de usuario
   - Maneja la entrada del teclado
   - Orquesta el procesamiento de ejercicios

2. **exercise_utils.py** - Lógica de ejercicios
   - Funciones puras sin dependencias de MediaPipe
   - Cálculo de ángulos entre puntos
   - Lógica de detección para cada ejercicio
   - Fácil de probar unitariamente

3. **test_exercise_tracker.py** - Suite de pruebas
   - 13 tests unitarios
   - Valida cálculos de ángulos
   - Verifica lógica de ejercicios
   - Prueba detección de repeticiones

### Estructura de Datos

#### Puntos de Referencia (Landmarks)
```python
points = {
    'left_shoulder': (x, y),
    'right_shoulder': (x, y),
    'left_elbow': (x, y),
    'right_elbow': (x, y),
    'left_wrist': (x, y),
    'right_wrist': (x, y),
    'left_hip': (x, y),
    'right_hip': (x, y),
}
```

#### Estados de Ejercicio
- `None` - Estado inicial
- `"down"` - Posición inicial/extendida
- `"up"` - Posición contraída/elevada
- `"flexed"` - Para extensiones de tríceps
- `"extended"` - Para extensiones de tríceps

## Detalles de los Ejercicios

### 1. Bicep Curl
**Ángulo medido:** Hombro-Codo-Muñeca (izquierdo)
- Extendido: > 160°
- Flexionado: < 40°
- **Repetición completa:** up → down (cuando vuelve a extender)

### 2. Shoulder Press
**Ángulo medido:** Hombro-Codo-Muñeca (izquierdo)
- Posición inicial: < 90°
- Extendido: > 160°
- **Repetición completa:** up → down

### 3. Lateral Raise
**Ángulo medido:** Cadera-Hombro-Codo (izquierdo)
- Brazos abajo: < 30°
- Brazos elevados: > 80°
- **Repetición completa:** up → down

### 4. Front Raise
**Ángulo medido:** Cadera-Hombro-Muñeca (izquierdo)
- Brazos abajo: < 30°
- Brazos al frente: > 80°
- **Repetición completa:** up → down

### 5. Hammer Curl
**Ángulo medido:** Hombro-Codo-Muñeca (izquierdo)
- Extendido: > 160°
- Flexionado: < 45°
- **Repetición completa:** up → down

### 6. Tricep Extension
**Ángulo medido:** Hombro-Codo-Muñeca (izquierdo)
- Flexionado: < 60°
- Extendido: > 160°
- **Repetición completa:** extended → flexed

## Cómo Funciona la Detección

### 1. Captura de Video
```python
cap = cv2.VideoCapture(0)  # Abre la cámara
frame = cv2.flip(frame, 1)  # Efecto espejo
```

### 2. Procesamiento con MediaPipe
```python
results = self.pose.process(image)
if results.pose_landmarks:
    # Procesar landmarks detectados
```

### 3. Cálculo de Ángulos
```python
angle = calculate_angle(punto_a, punto_b, punto_c)
# Usa arctan2 para calcular el ángulo entre vectores
```

### 4. Detección de Estado
- Compara el ángulo con umbrales predefinidos
- Determina el estado actual (up/down)
- Detecta transiciones de estado
- Cuenta repeticiones en transiciones específicas

### 5. Retroalimentación Visual
- Color verde: Forma correcta
- Color naranja: En progreso o necesita ajustes
- Mensajes específicos por ejercicio

## Extensibilidad

### Añadir un Nuevo Ejercicio

1. **Añadir a la lista de ejercicios:**
```python
self.exercises = {
    # ... ejercicios existentes ...
    "7": "Nombre del Nuevo Ejercicio"
}
```

2. **Crear función de procesamiento en exercise_utils.py:**
```python
def process_nuevo_ejercicio(points, current_stage):
    angle = calculate_angle(
        points['articulacion_1'],
        points['articulacion_2'],
        points['articulacion_3']
    )
    
    # Lógica de detección
    if angle > umbral_superior:
        new_stage = "estado_1"
    elif angle < umbral_inferior:
        new_stage = "estado_2"
    
    # Detectar repetición completa
    rep_completed = (current_stage == "estado_2" and new_stage == "estado_1")
    
    return rep_completed, feedback, new_stage
```

3. **Integrar en exercise_tracker.py:**
```python
elif self.exercise_name == "Nombre del Nuevo Ejercicio":
    rep_completed, feedback, new_stage = process_nuevo_ejercicio(points, self.exercise_stage)
```

4. **Añadir tests en test_exercise_tracker.py:**
```python
def test_nuevo_ejercicio_logic(self):
    points = {...}  # Puntos de prueba
    rep_completed, feedback, new_stage = process_nuevo_ejercicio(points, None)
    self.assertIsInstance(rep_completed, bool)
    self.assertIsInstance(feedback, str)
```

## Mejoras Futuras Sugeridas

1. **Detección Bilateral**
   - Rastrear ambos brazos simultáneamente
   - Detectar asimetrías

2. **Contador de Series**
   - Agrupar repeticiones en series
   - Temporizador de descanso entre series

3. **Guardado de Datos**
   - Exportar historial de entrenamientos
   - Gráficas de progreso

4. **Análisis de Velocidad**
   - Fase concéntrica vs excéntrica
   - Tiempo bajo tensión

5. **Detección de Errores Comunes**
   - Balanceo del cuerpo
   - Rango de movimiento incompleto
   - Velocidad inconsistente

6. **Múltiples Usuarios**
   - Perfiles de usuario
   - Comparación de métricas

## Troubleshooting

### La cámara no se detecta
```bash
# Linux: Verificar permisos de cámara
ls -l /dev/video*
# Añadir usuario al grupo video si es necesario
sudo usermod -a -G video $USER
```

### MediaPipe no detecta el cuerpo
- Verificar iluminación adecuada
- Asegurar que el cuerpo completo esté visible
- Aumentar distancia de la cámara
- Verificar que no hay objetos bloqueando la vista

### Rendimiento lento
- Reducir resolución de la cámara
- Cerrar aplicaciones en segundo plano
- Actualizar drivers de la GPU

### Repeticiones no se cuentan
- Verificar umbrales de ángulo para el ejercicio
- Asegurar movimiento completo del rango
- Revisar logs de feedback para entender el estado

## Licencia y Contribuciones

Ver README.md para información sobre licencia y cómo contribuir.

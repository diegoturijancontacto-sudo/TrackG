#!/bin/bash
# Script de demostración para probar la aplicación TrackG

echo "=== TrackG - Ejercicios con Seguimiento Corporal ==="
echo ""
echo "Este script instala las dependencias y ejecuta la aplicación."
echo ""

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 no está instalado."
    echo "Por favor instala Python 3.7 o superior."
    exit 1
fi

echo "✓ Python detectado: $(python3 --version)"
echo ""

# Preguntar si quiere instalar dependencias
read -p "¿Deseas instalar las dependencias? (s/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Ss]$ ]]; then
    echo "Instalando dependencias..."
    pip install -r requirements.txt
    echo ""
fi

# Mostrar información antes de ejecutar
echo "=== Instrucciones de Uso ==="
echo ""
echo "La aplicación se abrirá y usará tu cámara web."
echo ""
echo "Controles:"
echo "  1 - Bicep Curl (curl de bíceps)"
echo "  2 - Shoulder Press (press de hombros)"
echo "  3 - Lateral Raise (elevaciones laterales)"
echo "  4 - Front Raise (elevaciones frontales)"
echo "  5 - Hammer Curl (curl martillo)"
echo "  6 - Tricep Extension (extensiones de tríceps)"
echo "  Q - Salir"
echo ""
echo "Consejos:"
echo "  - Asegúrate de tener buena iluminación"
echo "  - Colócate de lado a la cámara"
echo "  - Mantén distancia de 1.5-2 metros"
echo ""

read -p "Presiona Enter para iniciar la aplicación..."

# Ejecutar la aplicación
python3 exercise_tracker.py

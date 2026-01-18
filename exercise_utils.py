"""
Utilidades y funciones auxiliares para el rastreador de ejercicios.
"""

import numpy as np
from typing import Dict, Tuple


def calculate_angle(a: Tuple, b: Tuple, c: Tuple) -> float:
    """
    Calcula el ángulo entre tres puntos.
    
    Args:
        a, b, c: Tuplas de coordenadas (x, y)
    
    Returns:
        Ángulo en grados
    """
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - \
              np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    
    if angle > 180.0:
        angle = 360 - angle
    
    return angle


def process_bicep_curl(points: Dict[str, Tuple[float, float]], current_stage: str) -> Tuple[bool, str, str]:
    """
    Procesa curl de bíceps (izquierdo).
    
    Args:
        points: Diccionario con coordenadas de puntos clave
        current_stage: Etapa actual del ejercicio
    
    Returns:
        (rep_completed, feedback, new_stage)
    """
    angle = calculate_angle(
        points['left_shoulder'],
        points['left_elbow'],
        points['left_wrist']
    )
    
    feedback = ""
    rep_completed = False
    new_stage = current_stage
    
    # Detectar fase del ejercicio
    if angle > 160:
        feedback = "Brazo extendido - ¡Bien!"
        if current_stage == "up":
            rep_completed = True
        new_stage = "down"
    elif angle < 40:
        feedback = "Flexión completa - ¡Perfecto!"
        new_stage = "up"
    elif 40 <= angle <= 90:
        feedback = "En movimiento..."
    else:
        feedback = "Mantén el codo estable"
    
    return rep_completed, feedback, new_stage


def process_shoulder_press(points: Dict[str, Tuple[float, float]], current_stage: str) -> Tuple[bool, str, str]:
    """
    Procesa press de hombros.
    
    Args:
        points: Diccionario con coordenadas de puntos clave
        current_stage: Etapa actual del ejercicio
    
    Returns:
        (rep_completed, feedback, new_stage)
    """
    elbow_angle = calculate_angle(
        points['left_shoulder'],
        points['left_elbow'],
        points['left_wrist']
    )
    
    feedback = ""
    rep_completed = False
    new_stage = current_stage
    
    if elbow_angle < 90:
        feedback = "Posición inicial - ¡Listo!"
        if current_stage == "up":
            rep_completed = True
        new_stage = "down"
    elif elbow_angle > 160:
        feedback = "Brazos extendidos - ¡Excelente!"
        new_stage = "up"
    else:
        feedback = "Presionando..."
    
    return rep_completed, feedback, new_stage


def process_lateral_raise(points: Dict[str, Tuple[float, float]], current_stage: str) -> Tuple[bool, str, str]:
    """
    Procesa elevaciones laterales.
    
    Args:
        points: Diccionario con coordenadas de puntos clave
        current_stage: Etapa actual del ejercicio
    
    Returns:
        (rep_completed, feedback, new_stage)
    """
    angle = calculate_angle(
        points['left_hip'],
        points['left_shoulder'],
        points['left_elbow']
    )
    
    feedback = ""
    rep_completed = False
    new_stage = current_stage
    
    if angle < 30:
        feedback = "Brazos abajo - ¡Bien!"
        if current_stage == "up":
            rep_completed = True
        new_stage = "down"
    elif angle > 80:
        feedback = "Brazos a la altura del hombro - ¡Perfecto!"
        new_stage = "up"
    else:
        feedback = "Elevando..."
    
    return rep_completed, feedback, new_stage


def process_front_raise(points: Dict[str, Tuple[float, float]], current_stage: str) -> Tuple[bool, str, str]:
    """
    Procesa elevaciones frontales.
    
    Args:
        points: Diccionario con coordenadas de puntos clave
        current_stage: Etapa actual del ejercicio
    
    Returns:
        (rep_completed, feedback, new_stage)
    """
    shoulder_wrist_angle = calculate_angle(
        points['left_hip'],
        points['left_shoulder'],
        points['left_wrist']
    )
    
    feedback = ""
    rep_completed = False
    new_stage = current_stage
    
    if shoulder_wrist_angle < 30:
        feedback = "Brazos abajo - ¡Listo!"
        if current_stage == "up":
            rep_completed = True
        new_stage = "down"
    elif shoulder_wrist_angle > 80:
        feedback = "Brazos al frente - ¡Excelente!"
        new_stage = "up"
    else:
        feedback = "Elevando al frente..."
    
    return rep_completed, feedback, new_stage


def process_hammer_curl(points: Dict[str, Tuple[float, float]], current_stage: str) -> Tuple[bool, str, str]:
    """
    Procesa curl martillo.
    
    Args:
        points: Diccionario con coordenadas de puntos clave
        current_stage: Etapa actual del ejercicio
    
    Returns:
        (rep_completed, feedback, new_stage)
    """
    angle = calculate_angle(
        points['left_shoulder'],
        points['left_elbow'],
        points['left_wrist']
    )
    
    feedback = ""
    rep_completed = False
    new_stage = current_stage
    
    if angle > 160:
        feedback = "Brazo extendido - ¡Bien!"
        if current_stage == "up":
            rep_completed = True
        new_stage = "down"
    elif angle < 45:
        feedback = "Flexión completa - ¡Perfecto!"
        new_stage = "up"
    else:
        feedback = "Contrayendo..."
    
    return rep_completed, feedback, new_stage


def process_tricep_extension(points: Dict[str, Tuple[float, float]], current_stage: str) -> Tuple[bool, str, str]:
    """
    Procesa extensiones de tríceps.
    
    Args:
        points: Diccionario con coordenadas de puntos clave
        current_stage: Etapa actual del ejercicio
    
    Returns:
        (rep_completed, feedback, new_stage)
    """
    angle = calculate_angle(
        points['left_shoulder'],
        points['left_elbow'],
        points['left_wrist']
    )
    
    feedback = ""
    rep_completed = False
    new_stage = current_stage
    
    if angle < 60:
        feedback = "Brazo flexionado - ¡Bien!"
        if current_stage == "extended":
            rep_completed = True
        new_stage = "flexed"
    elif angle > 160:
        feedback = "Extensión completa - ¡Excelente!"
        new_stage = "extended"
    else:
        feedback = "Extendiendo..."
    
    return rep_completed, feedback, new_stage

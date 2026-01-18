"""
Tests para el sistema de seguimiento de ejercicios.
Valida cálculos de ángulos y lógica de detección de ejercicios.
"""

import unittest
import numpy as np
from exercise_utils import (
    calculate_angle,
    process_bicep_curl,
    process_shoulder_press,
    process_lateral_raise,
    process_front_raise,
    process_hammer_curl,
    process_tricep_extension
)


class TestExerciseUtils(unittest.TestCase):
    """Tests para las funciones de utilidad."""
    
    def test_calculate_angle_90_degrees(self):
        """Test: Calcular ángulo de 90 grados."""
        # Puntos que forman un ángulo de 90 grados
        a = (0, 1)  # Punto superior
        b = (0, 0)  # Vértice
        c = (1, 0)  # Punto derecha
        
        angle = calculate_angle(a, b, c)
        self.assertAlmostEqual(angle, 90.0, places=1)
    
    def test_calculate_angle_180_degrees(self):
        """Test: Calcular ángulo de 180 grados (línea recta)."""
        a = (0, 0)
        b = (1, 0)
        c = (2, 0)
        
        angle = calculate_angle(a, b, c)
        self.assertAlmostEqual(angle, 180.0, places=1)
    
    def test_calculate_angle_45_degrees(self):
        """Test: Calcular ángulo de 45 grados."""
        a = (0, 1)
        b = (0, 0)
        c = (1, 1)
        
        angle = calculate_angle(a, b, c)
        self.assertAlmostEqual(angle, 45.0, places=1)
    
    def test_bicep_curl_extended_position(self):
        """Test: Bicep curl en posición extendida."""
        # Simular puntos de un brazo extendido (>160 grados)
        points = {
            'left_shoulder': (0.3, 0.3),
            'left_elbow': (0.3, 0.5),
            'left_wrist': (0.3, 0.7),
            'right_shoulder': (0.7, 0.3),
            'right_elbow': (0.7, 0.5),
            'right_wrist': (0.7, 0.7),
            'left_hip': (0.3, 0.8),
            'right_hip': (0.7, 0.8),
        }
        
        rep_completed, feedback, new_stage = process_bicep_curl(points, None)
        self.assertIn("extendido", feedback.lower())
        self.assertEqual(new_stage, "down")
    
    def test_bicep_curl_flexed_position(self):
        """Test: Bicep curl en posición flexionada."""
        # Simular puntos de un brazo flexionado (<40 grados)
        points = {
            'left_shoulder': (0.3, 0.3),
            'left_elbow': (0.3, 0.5),
            'left_wrist': (0.25, 0.35),  # Muñeca cerca del hombro
            'right_shoulder': (0.7, 0.3),
            'right_elbow': (0.7, 0.5),
            'right_wrist': (0.75, 0.35),
            'left_hip': (0.3, 0.8),
            'right_hip': (0.7, 0.8),
        }
        
        rep_completed, feedback, new_stage = process_bicep_curl(points, None)
        self.assertIn("flexión", feedback.lower())
        self.assertEqual(new_stage, "up")
    
    def test_shoulder_press_logic(self):
        """Test: Lógica básica de shoulder press."""
        points = {
            'left_shoulder': (0.3, 0.3),
            'left_elbow': (0.3, 0.5),
            'left_wrist': (0.3, 0.7),
            'right_shoulder': (0.7, 0.3),
            'right_elbow': (0.7, 0.5),
            'right_wrist': (0.7, 0.7),
            'left_hip': (0.3, 0.8),
            'right_hip': (0.7, 0.8),
        }
        
        rep_completed, feedback, new_stage = process_shoulder_press(points, None)
        self.assertIsInstance(rep_completed, bool)
        self.assertIsInstance(feedback, str)
        self.assertIsInstance(new_stage, str)
    
    def test_lateral_raise_logic(self):
        """Test: Lógica básica de lateral raise."""
        points = {
            'left_shoulder': (0.3, 0.3),
            'left_elbow': (0.3, 0.5),
            'left_wrist': (0.3, 0.7),
            'right_shoulder': (0.7, 0.3),
            'right_elbow': (0.7, 0.5),
            'right_wrist': (0.7, 0.7),
            'left_hip': (0.3, 0.8),
            'right_hip': (0.7, 0.8),
        }
        
        rep_completed, feedback, new_stage = process_lateral_raise(points, None)
        self.assertIsInstance(rep_completed, bool)
        self.assertIsInstance(feedback, str)
        self.assertIsInstance(new_stage, str)
    
    def test_front_raise_logic(self):
        """Test: Lógica básica de front raise."""
        points = {
            'left_shoulder': (0.3, 0.3),
            'left_elbow': (0.3, 0.5),
            'left_wrist': (0.3, 0.7),
            'right_shoulder': (0.7, 0.3),
            'right_elbow': (0.7, 0.5),
            'right_wrist': (0.7, 0.7),
            'left_hip': (0.3, 0.8),
            'right_hip': (0.7, 0.8),
        }
        
        rep_completed, feedback, new_stage = process_front_raise(points, None)
        self.assertIsInstance(rep_completed, bool)
        self.assertIsInstance(feedback, str)
        self.assertIsInstance(new_stage, str)
    
    def test_hammer_curl_logic(self):
        """Test: Lógica básica de hammer curl."""
        points = {
            'left_shoulder': (0.3, 0.3),
            'left_elbow': (0.3, 0.5),
            'left_wrist': (0.3, 0.7),
            'right_shoulder': (0.7, 0.3),
            'right_elbow': (0.7, 0.5),
            'right_wrist': (0.7, 0.7),
            'left_hip': (0.3, 0.8),
            'right_hip': (0.7, 0.8),
        }
        
        rep_completed, feedback, new_stage = process_hammer_curl(points, None)
        self.assertIsInstance(rep_completed, bool)
        self.assertIsInstance(feedback, str)
        self.assertIsInstance(new_stage, str)
    
    def test_tricep_extension_logic(self):
        """Test: Lógica básica de tricep extension."""
        points = {
            'left_shoulder': (0.3, 0.3),
            'left_elbow': (0.3, 0.5),
            'left_wrist': (0.3, 0.7),
            'right_shoulder': (0.7, 0.3),
            'right_elbow': (0.7, 0.5),
            'right_wrist': (0.7, 0.7),
            'left_hip': (0.3, 0.8),
            'right_hip': (0.7, 0.8),
        }
        
        rep_completed, feedback, new_stage = process_tricep_extension(points, None)
        self.assertIsInstance(rep_completed, bool)
        self.assertIsInstance(feedback, str)
        self.assertIsInstance(new_stage, str)
    
    def test_rep_completion_increments_counter(self):
        """Test: Completar una repetición incrementa el contador."""
        # Simular una repetición completa de bicep curl
        # Fase 1: Brazo extendido
        points_extended = {
            'left_shoulder': (0.3, 0.3),
            'left_elbow': (0.3, 0.5),
            'left_wrist': (0.3, 0.7),
            'right_shoulder': (0.7, 0.3),
            'right_elbow': (0.7, 0.5),
            'right_wrist': (0.7, 0.7),
            'left_hip': (0.3, 0.8),
            'right_hip': (0.7, 0.8),
        }
        
        # Fase 2: Brazo flexionado
        points_flexed = {
            'left_shoulder': (0.3, 0.3),
            'left_elbow': (0.3, 0.5),
            'left_wrist': (0.25, 0.35),
            'right_shoulder': (0.7, 0.3),
            'right_elbow': (0.7, 0.5),
            'right_wrist': (0.75, 0.35),
            'left_hip': (0.3, 0.8),
            'right_hip': (0.7, 0.8),
        }
        
        # Primera fase: brazo extendido (down)
        rep1, feedback1, stage1 = process_bicep_curl(points_extended, None)
        self.assertEqual(stage1, "down")
        
        # Segunda fase: brazo flexionado (up)
        rep2, feedback2, stage2 = process_bicep_curl(points_flexed, stage1)
        self.assertEqual(stage2, "up")
        
        # Tercera fase: volver a extender (debe completar rep)
        rep3, feedback3, stage3 = process_bicep_curl(points_extended, stage2)
        self.assertTrue(rep3)  # Se completa la repetición


class TestAngleCalculations(unittest.TestCase):
    """Tests específicos para cálculos de ángulos."""
    
    def test_angle_with_negative_coordinates(self):
        """Test: Calcular ángulos con coordenadas negativas."""
        a = (-1, 1)
        b = (0, 0)
        c = (1, -1)
        
        angle = calculate_angle(a, b, c)
        self.assertGreater(angle, 0)
        self.assertLessEqual(angle, 180)
    
    def test_angle_result_range(self):
        """Test: Los ángulos siempre están entre 0 y 180 grados."""
        test_cases = [
            ((0, 1), (0, 0), (1, 0)),
            ((1, 1), (0, 0), (1, -1)),
            ((0, 2), (0, 0), (2, 0)),
            ((-1, 0), (0, 0), (0, 1)),
        ]
        
        for a, b, c in test_cases:
            angle = calculate_angle(a, b, c)
            self.assertGreaterEqual(angle, 0)
            self.assertLessEqual(angle, 180)


def run_tests():
    """Ejecutar todos los tests."""
    unittest.main(argv=[''], verbosity=2, exit=False)


if __name__ == '__main__':
    print("=== Tests de TrackG - Sistema de Seguimiento de Ejercicios ===\n")
    run_tests()

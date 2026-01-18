import cv2
import mediapipe as mp
import numpy as np
import time
from typing import Dict, Tuple, Optional
from exercise_utils import (
    calculate_angle,
    process_bicep_curl,
    process_shoulder_press,
    process_lateral_raise,
    process_front_raise,
    process_hammer_curl,
    process_tricep_extension
)


class ExerciseTracker:
    """
    Clase para rastrear ejercicios de levantamiento de pesas usando MediaPipe.
    Detecta y cuenta repeticiones, mide ángulos y proporciona retroalimentación.
    """
    
    def __init__(self):
        # Inicializar MediaPipe
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils
        self.pose = self.mp_pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        
        # Variables de seguimiento
        self.exercise_name = "Bicep Curl"
        self.exercise_counter = 0
        self.exercise_stage = None
        self.last_rep_time = time.time()
        self.rep_duration = 0
        self.form_feedback = ""
        
        # Ejercicios disponibles
        self.exercises = {
            "1": "Bicep Curl",
            "2": "Shoulder Press",
            "3": "Lateral Raise",
            "4": "Front Raise",
            "5": "Hammer Curl",
            "6": "Tricep Extension"
        }
    

    def get_landmarks(self, landmarks) -> Dict[str, Tuple[float, float]]:
        """
        Extrae las coordenadas de los landmarks relevantes.
        
        Args:
            landmarks: Landmarks de MediaPipe
        
        Returns:
            Diccionario con coordenadas de puntos clave
        """
        return {
            'left_shoulder': (landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                            landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value].y),
            'right_shoulder': (landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                             landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y),
            'left_elbow': (landmarks[self.mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                          landmarks[self.mp_pose.PoseLandmark.LEFT_ELBOW.value].y),
            'right_elbow': (landmarks[self.mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                           landmarks[self.mp_pose.PoseLandmark.RIGHT_ELBOW.value].y),
            'left_wrist': (landmarks[self.mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                          landmarks[self.mp_pose.PoseLandmark.LEFT_WRIST.value].y),
            'right_wrist': (landmarks[self.mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                           landmarks[self.mp_pose.PoseLandmark.RIGHT_WRIST.value].y),
            'left_hip': (landmarks[self.mp_pose.PoseLandmark.LEFT_HIP.value].x,
                        landmarks[self.mp_pose.PoseLandmark.LEFT_HIP.value].y),
            'right_hip': (landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                         landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP.value].y),
        }
    
    def process_exercise(self, landmarks) -> None:
        """
        Procesa el ejercicio seleccionado actualmente.
        
        Args:
            landmarks: Landmarks de MediaPipe
        """
        points = self.get_landmarks(landmarks)
        
        rep_completed = False
        feedback = ""
        new_stage = self.exercise_stage
        
        # Procesar según el ejercicio seleccionado
        if self.exercise_name == "Bicep Curl":
            rep_completed, feedback, new_stage = process_bicep_curl(points, self.exercise_stage)
        elif self.exercise_name == "Shoulder Press":
            rep_completed, feedback, new_stage = process_shoulder_press(points, self.exercise_stage)
        elif self.exercise_name == "Lateral Raise":
            rep_completed, feedback, new_stage = process_lateral_raise(points, self.exercise_stage)
        elif self.exercise_name == "Front Raise":
            rep_completed, feedback, new_stage = process_front_raise(points, self.exercise_stage)
        elif self.exercise_name == "Hammer Curl":
            rep_completed, feedback, new_stage = process_hammer_curl(points, self.exercise_stage)
        elif self.exercise_name == "Tricep Extension":
            rep_completed, feedback, new_stage = process_tricep_extension(points, self.exercise_stage)
        
        self.form_feedback = feedback
        self.exercise_stage = new_stage
        
        # Actualizar contador si se completó una repetición
        if rep_completed:
            current_time = time.time()
            self.rep_duration = current_time - self.last_rep_time
            self.last_rep_time = current_time
            self.exercise_counter += 1
    
    def draw_ui(self, frame: np.ndarray) -> np.ndarray:
        """
        Dibuja la interfaz de usuario en el frame.
        
        Args:
            frame: Frame de video
        
        Returns:
            Frame con UI dibujada
        """
        height, width = frame.shape[:2]
        
        # Panel de información superior
        cv2.rectangle(frame, (0, 0), (width, 100), (245, 117, 16), -1)
        
        # Ejercicio actual
        cv2.putText(frame, f'Ejercicio: {self.exercise_name}',
                   (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        
        # Contador de repeticiones
        cv2.putText(frame, f'Repeticiones: {self.exercise_counter}',
                   (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        
        # Tiempo entre repeticiones
        if self.rep_duration > 0:
            cv2.putText(frame, f'Tiempo: {self.rep_duration:.1f}s',
                       (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Feedback de forma
        feedback_color = (0, 255, 0) if "Bien" in self.form_feedback or "Perfecto" in self.form_feedback or "Excelente" in self.form_feedback else (0, 165, 255)
        cv2.rectangle(frame, (0, height - 60), (width, height), (50, 50, 50), -1)
        cv2.putText(frame, self.form_feedback,
                   (10, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, feedback_color, 2)
        
        # Instrucciones
        cv2.putText(frame, 'Presiona 1-6 para cambiar ejercicio | Q para salir',
                   (10, height - 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        return frame
    
    def run(self):
        """
        Ejecuta la aplicación de seguimiento de ejercicios.
        """
        cap = cv2.VideoCapture(0)
        
        print("=== Aplicación de Seguimiento de Ejercicios ===")
        print("\nEjercicios disponibles:")
        for key, exercise in self.exercises.items():
            print(f"  {key}: {exercise}")
        print("\nPresiona Q para salir\n")
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("No se puede acceder a la cámara")
                break
            
            # Voltear el frame horizontalmente para efecto espejo
            frame = cv2.flip(frame, 1)
            
            # Convertir BGR a RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            
            # Procesar con MediaPipe
            results = self.pose.process(image)
            
            # Convertir de nuevo a BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            # Procesar landmarks si se detectan
            if results.pose_landmarks:
                # Dibujar landmarks
                self.mp_drawing.draw_landmarks(
                    image,
                    results.pose_landmarks,
                    self.mp_pose.POSE_CONNECTIONS,
                    self.mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                    self.mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                )
                
                # Procesar ejercicio
                self.process_exercise(results.pose_landmarks.landmark)
            
            # Dibujar UI
            image = self.draw_ui(image)
            
            # Mostrar frame
            cv2.imshow('TrackG - Seguimiento de Ejercicios', image)
            
            # Manejo de teclas
            key = cv2.waitKey(10) & 0xFF
            if key == ord('q'):
                break
            elif chr(key) in self.exercises:
                self.exercise_name = self.exercises[chr(key)]
                self.exercise_counter = 0
                self.exercise_stage = None
                self.form_feedback = ""
                print(f"\nEjercicio cambiado a: {self.exercise_name}")
        
        cap.release()
        cv2.destroyAllWindows()
        self.pose.close()


def main():
    """
    Función principal para ejecutar la aplicación.
    """
    tracker = ExerciseTracker()
    tracker.run()


if __name__ == "__main__":
    main()

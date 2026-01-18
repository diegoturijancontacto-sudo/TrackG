// TrackG - Exercise Tracker JavaScript

// Variables globales
let pose;
let camera;
let exerciseName = "Bicep Curl";
let exerciseCounter = 0;
let exerciseStage = null;
let lastRepTime = Date.now();
let repDuration = 0;
let formFeedback = "";

// Mapeo de ejercicios - se cargará desde el servidor
let exercises = {
    "1": "Bicep Curl",
    "2": "Shoulder Press",
    "3": "Lateral Raise",
    "4": "Front Raise",
    "5": "Hammer Curl",
    "6": "Tricep Extension"
};

// Función para calcular ángulo entre tres puntos
function calculateAngle(a, b, c) {
    const radians = Math.atan2(c.y - b.y, c.x - b.x) - Math.atan2(a.y - b.y, a.x - b.x);
    let angle = Math.abs(radians * 180.0 / Math.PI);
    
    if (angle > 180.0) {
        angle = 360 - angle;
    }
    
    return angle;
}

// Función para procesar Bicep Curl
function processBicepCurl(landmarks, currentStage) {
    const leftShoulder = landmarks[11];
    const leftElbow = landmarks[13];
    const leftWrist = landmarks[15];
    
    const angle = calculateAngle(leftShoulder, leftElbow, leftWrist);
    
    let repCompleted = false;
    let feedback = "";
    let newStage = currentStage;
    
    if (angle > 160) {
        newStage = "down";
        feedback = "Brazo extendido";
    }
    
    if (angle < 40 && currentStage === "down") {
        newStage = "up";
        feedback = "¡Bien! Flexión completa";
    }
    
    if (currentStage === "up" && newStage === "down") {
        repCompleted = true;
        feedback = "¡Repetición completa!";
    }
    
    return { repCompleted, feedback, newStage };
}

// Función para procesar Shoulder Press
function processShoulderPress(landmarks, currentStage) {
    const leftShoulder = landmarks[11];
    const leftElbow = landmarks[13];
    const leftWrist = landmarks[15];
    
    const angle = calculateAngle(leftShoulder, leftElbow, leftWrist);
    
    let repCompleted = false;
    let feedback = "";
    let newStage = currentStage;
    
    if (angle < 90) {
        newStage = "down";
        feedback = "Posición inicial";
    }
    
    if (angle > 160 && currentStage === "down") {
        newStage = "up";
        feedback = "¡Perfecto! Extensión completa";
    }
    
    if (currentStage === "up" && newStage === "down") {
        repCompleted = true;
        feedback = "¡Repetición completa!";
    }
    
    return { repCompleted, feedback, newStage };
}

// Función para procesar Lateral Raise
function processLateralRaise(landmarks, currentStage) {
    const leftHip = landmarks[23];
    const leftShoulder = landmarks[11];
    const leftElbow = landmarks[13];
    
    const angle = calculateAngle(leftHip, leftShoulder, leftElbow);
    
    let repCompleted = false;
    let feedback = "";
    let newStage = currentStage;
    
    if (angle < 30) {
        newStage = "down";
        feedback = "Brazos abajo";
    }
    
    if (angle > 80 && currentStage === "down") {
        newStage = "up";
        feedback = "¡Excelente! Elevación completa";
    }
    
    if (currentStage === "up" && newStage === "down") {
        repCompleted = true;
        feedback = "¡Repetición completa!";
    }
    
    return { repCompleted, feedback, newStage };
}

// Función para procesar Front Raise
function processFrontRaise(landmarks, currentStage) {
    const leftHip = landmarks[23];
    const leftShoulder = landmarks[11];
    const leftWrist = landmarks[15];
    
    const angle = calculateAngle(leftHip, leftShoulder, leftWrist);
    
    let repCompleted = false;
    let feedback = "";
    let newStage = currentStage;
    
    if (angle < 30) {
        newStage = "down";
        feedback = "Brazos abajo";
    }
    
    if (angle > 80 && currentStage === "down") {
        newStage = "up";
        feedback = "¡Bien! Elevación frontal completa";
    }
    
    if (currentStage === "up" && newStage === "down") {
        repCompleted = true;
        feedback = "¡Repetición completa!";
    }
    
    return { repCompleted, feedback, newStage };
}

// Función para procesar Hammer Curl
function processHammerCurl(landmarks, currentStage) {
    const leftShoulder = landmarks[11];
    const leftElbow = landmarks[13];
    const leftWrist = landmarks[15];
    
    const angle = calculateAngle(leftShoulder, leftElbow, leftWrist);
    
    let repCompleted = false;
    let feedback = "";
    let newStage = currentStage;
    
    if (angle > 160) {
        newStage = "down";
        feedback = "Brazo extendido";
    }
    
    if (angle < 45 && currentStage === "down") {
        newStage = "up";
        feedback = "¡Perfecto! Curl martillo completo";
    }
    
    if (currentStage === "up" && newStage === "down") {
        repCompleted = true;
        feedback = "¡Repetición completa!";
    }
    
    return { repCompleted, feedback, newStage };
}

// Función para procesar Tricep Extension
function processTricepExtension(landmarks, currentStage) {
    const leftShoulder = landmarks[11];
    const leftElbow = landmarks[13];
    const leftWrist = landmarks[15];
    
    const angle = calculateAngle(leftShoulder, leftElbow, leftWrist);
    
    let repCompleted = false;
    let feedback = "";
    let newStage = currentStage;
    
    if (angle < 60) {
        newStage = "flexed";
        feedback = "Posición flexionada";
    }
    
    if (angle > 160 && currentStage === "flexed") {
        newStage = "extended";
        feedback = "¡Excelente! Extensión completa";
    }
    
    if (currentStage === "extended" && newStage === "flexed") {
        repCompleted = true;
        feedback = "¡Repetición completa!";
    }
    
    return { repCompleted, feedback, newStage };
}

// Función para procesar el ejercicio seleccionado
function processExercise(landmarks) {
    let result = { repCompleted: false, feedback: "", newStage: exerciseStage };
    
    switch (exerciseName) {
        case "Bicep Curl":
            result = processBicepCurl(landmarks, exerciseStage);
            break;
        case "Shoulder Press":
            result = processShoulderPress(landmarks, exerciseStage);
            break;
        case "Lateral Raise":
            result = processLateralRaise(landmarks, exerciseStage);
            break;
        case "Front Raise":
            result = processFrontRaise(landmarks, exerciseStage);
            break;
        case "Hammer Curl":
            result = processHammerCurl(landmarks, exerciseStage);
            break;
        case "Tricep Extension":
            result = processTricepExtension(landmarks, exerciseStage);
            break;
    }
    
    formFeedback = result.feedback;
    exerciseStage = result.newStage;
    
    if (result.repCompleted) {
        const currentTime = Date.now();
        repDuration = (currentTime - lastRepTime) / 1000;
        lastRepTime = currentTime;
        exerciseCounter++;
        updateUI();
    }
    
    updateFeedback();
}

// Función para actualizar la UI
function updateUI() {
    document.getElementById('current-exercise').textContent = exerciseName;
    document.getElementById('rep-counter').textContent = exerciseCounter;
    document.getElementById('rep-time').textContent = repDuration.toFixed(1) + 's';
}

// Función para actualizar el feedback
function updateFeedback() {
    const feedbackElement = document.getElementById('feedback');
    feedbackElement.textContent = formFeedback;
    
    if (formFeedback.includes('¡Bien!') || formFeedback.includes('¡Perfecto!') || 
        formFeedback.includes('¡Excelente!') || formFeedback.includes('completa')) {
        feedbackElement.className = 'feedback good';
    } else {
        feedbackElement.className = 'feedback warning';
    }
}

// Función para cambiar ejercicio
function changeExercise(exerciseNumber) {
    exerciseName = exercises[exerciseNumber];
    exerciseCounter = 0;
    exerciseStage = null;
    formFeedback = "";
    repDuration = 0;
    lastRepTime = Date.now();
    
    // Actualizar botones activos
    document.querySelectorAll('.exercise-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    document.querySelector(`[data-exercise="${exerciseNumber}"]`).classList.add('active');
    
    updateUI();
    updateFeedback();
    
    console.log(`Ejercicio cambiado a: ${exerciseName}`);
}

// Callback para procesar resultados de MediaPipe
function onResults(results) {
    const videoElement = document.getElementById('video');
    const canvasElement = document.getElementById('output-canvas');
    const canvasCtx = canvasElement.getContext('2d');
    
    // Ajustar tamaño del canvas
    canvasElement.width = videoElement.videoWidth;
    canvasElement.height = videoElement.videoHeight;
    
    // Limpiar canvas
    canvasCtx.save();
    canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);
    
    // Dibujar imagen de fondo
    canvasCtx.drawImage(results.image, 0, 0, canvasElement.width, canvasElement.height);
    
    // Procesar landmarks si se detectan
    if (results.poseLandmarks) {
        // Dibujar conectores
        window.drawConnectors(canvasCtx, results.poseLandmarks, window.POSE_CONNECTIONS, {
            color: '#00FF00',
            lineWidth: 4
        });
        
        // Dibujar landmarks
        window.drawLandmarks(canvasCtx, results.poseLandmarks, {
            color: '#FF0000',
            lineWidth: 2,
            radius: 6
        });
        
        // Procesar ejercicio
        processExercise(results.poseLandmarks);
    }
    
    canvasCtx.restore();
}

// Inicializar MediaPipe Pose
function initializePose() {
    pose = new Pose({
        locateFile: (file) => {
            return `https://cdn.jsdelivr.net/npm/@mediapipe/pose/${file}`;
        }
    });
    
    pose.setOptions({
        modelComplexity: 1,
        smoothLandmarks: true,
        enableSegmentation: false,
        smoothSegmentation: false,
        minDetectionConfidence: 0.5,
        minTrackingConfidence: 0.5
    });
    
    pose.onResults(onResults);
}

// Inicializar cámara
function initializeCamera() {
    const videoElement = document.getElementById('video');
    
    camera = new Camera(videoElement, {
        onFrame: async () => {
            await pose.send({ image: videoElement });
        },
        width: 1280,
        height: 720
    });
    
    camera.start()
        .catch((error) => {
            console.error('Error al acceder a la cámara:', error);
            const feedbackElement = document.getElementById('feedback');
            feedbackElement.textContent = 'Error: No se puede acceder a la cámara. Por favor, permite el acceso a la cámara en tu navegador.';
            feedbackElement.className = 'feedback warning';
            feedbackElement.style.display = 'block';
        });
}

// Inicializar la aplicación cuando se carga la página
window.addEventListener('load', () => {
    console.log('Inicializando TrackG...');
    console.log('Ejercicios disponibles:', exercises);
    initializePose();
    initializeCamera();
    updateUI();
    console.log('TrackG inicializado correctamente');
});

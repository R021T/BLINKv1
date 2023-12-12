from django.shortcuts import render
import cv2
import dlib
import time
import math

# Create your views here.
code={
    ".-" : "A",
    "-..." : "B",
    "-.-." : "C",
    "-.." : "D",
    "." : "E",
    "..-." : "F",
    "--." : "G",
    "...." : "H",
    ".." : "I",
    ".---" : "J",
    "-.-" : "K",
    ".-.." : "L",
    "--" : "M",
    "-." : "N",
    "---" : "O",
    ".--." : "P",
    "--.-" : "Q",
    ".-." : "R",
    "..." : "S",
    "-" : "T",
    "..-" : "U",
    "...-" : "V",
    ".--" : "W",
    "-..-" : "X",
    "-.--" : "Y",
    "--.." : "Z",
    "-----" : "0",
    ".----" : "1",
    "..---" : "2",
    "...--" : "3",
    "....-" : "4",
    "....." : "5",
    "-...." : "6",
    "--..." : "7",
    "---.." : "8",
    "----." : "9"
}

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
EAR_THRESHOLD = 0.2
CONSECUTIVE_FRAMES = 3
cap = None
word=""

def home(request):
    return render(request,'home.html')
    
def start(request):
    global cap,word
    if cap is None:
        cap = cv2.VideoCapture(0)
        word = ""
    blink_count = 0
    last_blink_time = time.time()
    last_blink_start = None
    blink_history = ""
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        for face in faces:
            landmarks = predictor(gray, face)
            left_eye = [landmarks.part(i) for i in range(36, 42)]
            right_eye = [landmarks.part(i) for i in range(42, 48)]
            left_ear = eye_aspect_ratio(left_eye)
            right_ear = eye_aspect_ratio(right_eye)
            avg_ear = (left_ear + right_ear) / 2.0
            if avg_ear < EAR_THRESHOLD:
                if last_blink_start is None:
                    last_blink_start = time.time()
            else:
                if last_blink_start is not None:
                    blink_count += 1
                    last_blink_time = time.time()
                    blink_duration = time.time() - last_blink_start
                    last_blink_start = None
                    if blink_duration > 0.5:
                        if blink_history in code:
                            word+=code[blink_history]
                        blink_history=""
                    elif blink_duration > 0.2:
                        blink_history += "-"
                    else:
                        blink_history += "."
                    print(f"Blink {blink_count}: {blink_history} ({blink_duration:.2f} seconds) Word= {word}")
        cv2.putText(frame, f"Blinks: {blink_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow("Blink Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return render(request,'home.html')

def eye_aspect_ratio(eye):
    vertical_dist_1 = math.sqrt((eye[1].x - eye[5].x)**2 + (eye[1].y - eye[5].y)**2)
    vertical_dist_2 = math.sqrt((eye[2].x - eye[4].x)**2 + (eye[2].y - eye[4].y)**2)
    horizontal_dist = math.sqrt((eye[0].x - eye[3].x)**2 + (eye[0].y - eye[3].y)**2)
    ear = (vertical_dist_1 + vertical_dist_2) / (2.0 * horizontal_dist)
    return ear

def stop(request):
    global cap,word
    if cap is not None:
        cap.release()
        cap = None
    cv2.destroyAllWindows()
    return render(request,'home.html',{'word':word})

def clear(request):
    return render(request,'home.html',{'word':''})
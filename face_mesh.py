import cv2
import mediapipe as mp
import imutils
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1, color=(0, 255, 0)) 

cap = cv2.VideoCapture(0)

with mp_face_mesh.FaceMesh(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as face_mesh:
    while cap.isOpened():
        success, image = cap.read()
        image = imutils.resize(image, width=720, height=720)
        if not success:
            print("ignore")
            continue
        
        flip_image = cv2.flip(image,1)
        
        image_rgb = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image_rgb.flags.writeable = False
        results = face_mesh.process(image_rgb)

        image_rgb.flags.writeable = True
        image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)
        cv2.imshow("original", flip_image)

        black_background = np.zeros_like(image_bgr)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=black_background,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=drawing_spec,
                    connection_drawing_spec=drawing_spec
                )

        cv2.imshow("facemesh", black_background)
        
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

cap.release()
cv2.destroyAllWindows()

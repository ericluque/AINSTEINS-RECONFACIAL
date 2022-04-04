import cv2
from mtcnn.mtcnn import MTCNN

detector = MTCNN()

cap = cv2.VideoCapture('pessoas.mp4')

while True:
    ret, frame = cap.read()

    if ret:
    	faces = detector.detect_faces(frame)
    	for face in faces:
            # print(face)
            cv2.rectangle(frame, face['box'], 255, 2)

    	cv2.imshow('window', frame)
	    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# {
# 	'box': [422, 113, 76, 99], 
# 	'confidence': 0.7092751264572144, 
# 	'keypoints': {
# 		'left_eye': (443, 152), 
# 		'right_eye': (474, 151), 
# 		'nose': (453, 173), 
# 		'mouth_left': (445, 190), 
# 		'mouth_right': (472, 188)
# 	}
# }
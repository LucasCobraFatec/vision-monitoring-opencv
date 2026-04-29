import cv2

xml_haar_cascade = 'data/haarcascade_frontalface_alt2.xml'

#classificador carregado
faceClassifier = cv2.CascadeClassifier(xml_haar_cascade)


#iniciar o video

capture = cv2.VideoCapture('data/video_teste.mp4')

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    ret, frame_color = capture.read()

    if not ret:
        print("Fim do vídeo ou erro na captura.")
        break

    gray = cv2.cvtColor(frame_color, cv2.COLOR_BGR2GRAY)

    faces = faceClassifier.detectMultiScale(gray)

    for x,y,w,h in faces:
            cv2.rectangle(frame_color,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('color', frame_color)
    #cv2.imshow('gray', gray)

    if cv2.waitKey(20) & 0xFF == ord('q'): break




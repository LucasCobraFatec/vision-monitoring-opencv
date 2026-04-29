import cv2

webcam = cv2.VideoCapture('data/video_teste.mp4')

if webcam.isOpened():

    validacao, frame = webcam.read()

    while validacao:
        validacao, frame = webcam.read()
        if validacao:
            #cinza = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #converter para tons de cinza
            #bordas =cv2.Canny(cinza,50,150)
            #cv2.imshow("Apenas Bordas",bordas)

            #area  de um retangulo azul que simula "zona proibida"
            cv2.rectangle(frame,(100,100),(300,400),(255,0,0),3) #imagem/pronto_inicial/ponto_final/cor_RGB/espessura

            cv2.putText(frame,"AREA MONITORADA", (100,90),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),2)

            cv2.imshow('Monitoramento', frame) 

            cv2.imwrite("results/Foto.jpg",frame)


            #cv2.imwrite("results/Fotocinza.jpg",cinza) #capturando a imagem em cinza



        else:
            break

        key = cv2.waitKey(5)
        if key == 27: break  #tecla ESC para sair




webcam.release()
cv2.destroyAllWindows()

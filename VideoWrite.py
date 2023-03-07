# Importar librerias
import cv2

# Creamos la Video Captura
cap = cv2.VideoCapture(0)
ancho = int(cap.get(3))
alto = int(cap.get(4))

print(ancho, alto)

# cv2.VideoWriter(Nombre, Codificacion, FPS, Tamaño)
out = cv2.VideoWriter('Video2.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 10, (ancho, alto))

# Creamos un ciclo para ejecutar nuestros Frames
while True:
    # Leemos los fotogramas
    ret, frame = cap.read()

    # Guardamos el video
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    out.write(frame)

    # Mostramos los Frames
    cv2.imshow("VIDEO CAPTURA", frame)

    # Cerramos con lectura de teclado
    t = cv2.waitKey(1)
    if t == 27:
        break

# Liberamos la VideoCaptura
cap.release()
# Cerramos la ventana
cv2.destroyAllWindows()
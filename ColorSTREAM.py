# Importamos librerias
import cv2

# Creamos la Video Captura
cap = cv2.VideoCapture(0)

# Creamos un ciclo para ejecutar nuestros Frames
while True:
    # Leemos los fotogramas
    ret, frame = cap.read()

    # Conversiones
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    edg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    print(ret)

    # Mostramos los Frames
    cv2.imshow("VIDEO CAPTURA RGB", frame)
    cv2.imshow("VIDEO CAPTURA HSV", hsv)
    cv2.imshow("VIDEO CAPTURA EDG", edg)

    # Cerramos con lectura de teclado
    t = cv2.waitKey(1)
    if t == 27:
        break

# Liberamos la VideoCaptura
cap.release()
# Cerramos la ventana
cv2.destroyAllWindows()
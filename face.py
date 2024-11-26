import cv2
import numpy as np
import time
import serial
from PIL import Image, ImageOps

# Funkcja do obsługi LED (za pomocą portu szeregowego)
def control_led(port, action):
    try:
        ser = serial.Serial(port, 9600)
        if action == "ON":
            ser.write(b'LED_ON')
        elif action == "OFF":
            ser.write(b'LED_OFF')
        ser.close()
    except Exception as e:
        print(f"Error controlling LED: {e}")

# Funkcja do robienia zdjęcia
def capture_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Nie udało się połączyć z kamerą")
        return None

    # Uruchamiamy LED
    control_led('COM3', 'ON')
    time.sleep(0.5)  # LED miga przez 0.5 sekundy
    control_led('COM3', 'OFF')

    ret, frame = cap.read()
    cap.release()

    if ret:
        return frame
    else:
        print("Nie udało się zrobić zdjęcia.")
        return None

# Funkcja do porównania twarzy z obrazem Józefa Czechowicza
def compare_faces(image1, image2):
    # Zakładamy, że mamy plik .xml do detekcji twarzy (można użyć własnego)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Konwersja zdjęć na szaro
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Wykrywanie twarzy na obu zdjęciach
    faces1 = face_cascade.detectMultiScale(gray1, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    faces2 = face_cascade.detectMultiScale(gray2, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces1) == 0 or len(faces2) == 0:
        return 0  # Brak twarzy, nie można porównać

    # Załóżmy, że używamy tylko pierwszej wykrytej twarzy
    (x1, y1, w1, h1) = faces1[0]
    (x2, y2, w2, h2) = faces2[0]

    face1 = gray1[y1:y1+h1, x1:x1+w1]
    face2 = gray2[y2:y2+h2, x2:x2+w2]

    # Porównanie twarzy: można użyć np. prostego porównania histogramów
    hist1 = cv2.calcHist([face1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([face2], [0], None, [256], [0, 256])

    # Normalizacja histogramów
    cv2.normalize(hist1, hist1, 0, 255, cv2.NORM_MINMAX)
    cv2.normalize(hist2, hist2, 0, 255, cv2.NORM_MINMAX)

    # Obliczanie różnicy histogramów
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity * 100  # Zwracamy podobieństwo w procentach

# Funkcja do nakładania efektu na zdjęcie
def apply_effect(image):
    # Zamiana na rysunek ołówkiem
    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert_img = cv2.bitwise_not(grey_img)
    sketch = cv2.divide(grey_img, 255 - invert_img, scale=256)

    return sketch

# Funkcja do drukowania wyniku
def print_result(image, similarity):
    # Zapisz obraz do pliku
    cv2.imwrite('output_image.jpg', image)

    # Wydrukuj wynik - zakłada się, że drukarka jest podłączona
    print(f"Podobieństwo do Józefa Czechowicza: {similarity}%")
    # Zakładając, że drukarka działa przez system Windows/Linux
    # Trzeba dostosować kod do drukarki (tutaj można użyć polecenia systemowego)
    # print("Drukowanie...")
    # system("lp output_image.jpg")

# Główna funkcja programu
def main():
    print("Witaj w fotobudce Czechowicza!")
    
    # Ładowanie zdjęcia Józefa Czechowicza
    czechowicz_image = cv2.imread('czechowicz.jpg')  # Plik z obrazem Józefa Czechowicza

    # Ekran 1: Start
    input("Naciśnij Enter, aby rozpocząć robienie zdjęcia...")

    # Ekran 2: Robienie zdjęcia
    photo = capture_image()
    if photo is None:
        return

    # Ekran 3: Akceptacja zdjęcia
    cv2.imshow("Zrobione zdjęcie", photo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Porównanie zdjęcia z Czechowiczem
    similarity = compare_faces(photo, czechowicz_image)

    # Ekran 4: Wynik
    print(f"Twoje podobieństwo do Józefa Czechowicza: {similarity}%")

    # Zastosowanie efektu na zdjęciu
    modified_image = apply_effect(photo)

    # Drukowanie wyników
    print_result(modified_image, similarity)

if __name__ == '__main__':
    main()

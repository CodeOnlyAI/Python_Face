# Fotobudka Czechowicza

Projekt fotobudki, która identyfikuje podobieństwo użytkownika do poety Józefa Czechowicza na podstawie rozpoznawania twarzy. Program przechodzi przez następujące etapy: robienie zdjęcia użytkownika, porównanie twarzy z obrazem Czechowicza, generowanie wyniku podobieństwa oraz wydrukowanie zmodyfikowanego zdjęcia użytkownika.

## Spis treści

- [Opis](#opis)
- [Wymagania](#wymagania)
- [Instalacja](#instalacja)
- [Użycie](#użycie)
- [Struktura kodu](#struktura-kodu)
- [Konfiguracja sprzętu](#konfiguracja-sprzętu)
- [Licencja](#licencja)

## Opis

Fotobudka Czechowicza to interaktywna aplikacja, która pozwala użytkownikom zrobić zdjęcie i porównać swoje podobieństwo do legendarnego poety Józefa Czechowicza. Program wykorzystuje algorytm rozpoznawania twarzy, aby ocenić, jak bardzo osoba na zdjęciu przypomina wyglądem Czechowicza.

Projekt bazuje na Pythonie i wykorzystuje popularne biblioteki do przetwarzania obrazu i rozpoznawania twarzy:

- **OpenCV** do przechwytywania obrazu z kamery oraz obróbki zdjęć.
- **Dlib** lub **OpenCV's face recognition** do porównania twarzy.
- **Pillow** do nakładania efektów artystycznych na zdjęcia (np. efekt ołówka).
- **Pyserial** do kontrolowania diody LED podłączonej do USB.

Aplikacja umożliwia również wydrukowanie finalnego obrazu z procentową zgodnością, dzięki czemu użytkownicy mogą zobaczyć, jak bardzo przypominają Czechowicza.

## Wymagania

### Oprogramowanie:

- **Python 3.x** (zalecana wersja: 3.6+)
- **Biblioteki Pythona**:
  - `opencv-python` - do obsługi kamery i analizy obrazu.
  - `dlib` - do wykrywania twarzy.
  - `Pillow` - do obróbki obrazów (efekty artystyczne).
  - `pyserial` - do komunikacji z portem szeregowym (sterowanie diodą LED).
  
Aby zainstalować wymagane biblioteki, uruchom w terminalu:

```bash
pip install opencv-python dlib pillow pyserial
Sprzęt:
Komputer (Windows 10 lub Linux) z procesorem Intel, np. Pipo X9.
Kamera internetowa (np. Logitech C270).
Dioda LED na USB (do zasygnalizowania robienia zdjęcia).
Drukarka (np. Brother 5100N) podłączona przez USB do drukowania wyników.
Instalacja
Zainstaluj wymagane biblioteki:

Aby zainstalować wszystkie wymagane biblioteki Pythona, uruchom poniższe polecenie:

bash
Skopiuj kod
pip install opencv-python dlib pillow pyserial
Pobierz zdjęcie Józefa Czechowicza:

Pobierz obraz Józefa Czechowicza i umieść go w katalogu głównym projektu jako czechowicz.jpg. Może to być zdjęcie lub portret w wysokiej jakości.

Skonfiguruj sprzęt:

Podłącz kamerę do portu USB komputera.
Podłącz LED do portu USB i upewnij się, że jest kontrolowany przez port szeregowy (zobacz sekcję "Sterowanie LED").
Upewnij się, że drukarka jest podłączona i działa prawidłowo (możesz używać systemowego narzędzia do drukowania, np. lp w Linuxie).
Przygotowanie pliku z kodem:

Upewnij się, że masz skrypt Pythona, np. fotobudka.py w katalogu głównym.
Umieść obraz czechowicz.jpg w tym samym katalogu.
Użycie
Uruchom program:

Uruchom aplikację w terminalu:

bash
Skopiuj kod
python fotobudka.py
Przebieg użytkownika:

Ekran powitalny wyświetli informację o rozpoczęciu procesu.
Program uruchomi kamerę i zrobi zdjęcie użytkownika.
LED na USB mignie, sygnalizując, że zdjęcie zostało wykonane.
Użytkownik zatwierdza zdjęcie lub wykonuje nowe.
Program porówna twarz użytkownika z obrazem Józefa Czechowicza.
Zostanie wyświetlony wynik podobieństwa (np. "Podobieństwo do Józefa Czechowicza: 78%").
Program nałoży efekt artystyczny na zdjęcie (np. rysunek ołówkiem).
Wydrukowanie zdjęcia z efektem oraz wynik podobieństwa.
Struktura kodu
fotobudka.py - Główny skrypt Pythona, który zawiera logikę aplikacji. Obsługuje robienie zdjęcia, rozpoznawanie twarzy, generowanie wyników i wydrukowanie efektów.
czechowicz.jpg - Obraz Józefa Czechowicza, który jest używany do porównania twarzy.
output_image.jpg - Zmienione zdjęcie użytkownika z efektem artystycznym, zapisane po zakończeniu procesu.
Konfiguracja sprzętu
Kamera:
Podłącz kamerę do komputera.
Sprawdź, czy kamera jest rozpoznawana przez OpenCV (np. cv2.VideoCapture()).
LED:
LED jest sterowany przez port szeregowy. Należy dostosować port COM w funkcji control_led w kodzie (zmień COM3 na odpowiedni port).
Drukarka:
Drukarka powinna być podłączona przez USB.
Możesz użyć systemowego narzędzia do drukowania, jak lp w systemie Linux.

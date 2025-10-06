#!/usr/bin/env python3
# face_detect_haar.py
# Detección de caras con Haar Cascade (OpenCV)

import cv2
import argparse
import sys
from pathlib import Path

def build_args():
    p = argparse.ArgumentParser(description="Detección de caras con Haar Cascade (OpenCV)")
    p.add_argument("--source", "-s",
                   help="Fuente de vídeo/imagen. Puede ser ruta a imagen/vídeo o índice de cámara (0,1...). "
                        "Si se omite, usa la webcam 0 por defecto.",
                   default="0")
    p.add_argument("--cascade",
                   help="Ruta al clasificador Haar. Por defecto usa el 'haarcascade_frontalface_default.xml' de OpenCV.",
                   default=str(Path(cv2.data.haarcascades) / "haarcascade_frontalface_default.xml"))
    p.add_argument("--scale-factor", type=float, default=1.1,
                   help="Factor de escala para el algoritmo (típico 1.05–1.4).")
    p.add_argument("--min-neighbors", type=int, default=5,
                   help="Min neighbors para filtrar detecciones falsas (típico 3–8).")
    p.add_argument("--min-size", type=int, default=24,
                   help="Tamaño mínimo del rostro en píxeles (cuadrado).")
    p.add_argument("--gray-eq", action="store_true",
                   help="Aplicar ecualización de histograma al gris (puede mejorar en baja luz).")
    p.add_argument("--write", "-w", metavar="out.mp4",
                   help="Guardar la salida con cajas en un archivo de vídeo.")
    p.add_argument("--display", "-d", action="store_true",
                   help="Mostrar ventana con resultados (útil si la fuente es archivo).")
    return p.parse_args()

def open_source(src_str):
    # Si es un número (webcam)
    if src_str.isdigit():
        return cv2.VideoCapture(int(src_str)), True
    # Si es ruta a archivo
    path = Path(src_str)
    if not path.exists():
        print(f"[ERROR] No se encontró la fuente: {src_str}")
        sys.exit(1)
    # ¿Imagen o vídeo?
    if path.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp"]:
        img = cv2.imread(str(path))
        if img is None:
            print(f"[ERROR] No se pudo leer la imagen: {src_str}")
            sys.exit(1)
        return img, False  # devolvemos la imagen y flag de flujo False
    # Vídeo
    cap = cv2.VideoCapture(str(path))
    return cap, True

def main():
    args = build_args()

    # Cargar cascada
    cascade_path = Path(args.cascade)
    if not cascade_path.exists():
        print(f"[ERROR] No se encontró el clasificador Haar en: {cascade_path}")
        sys.exit(1)
    face_cascade = cv2.CascadeClassifier(str(cascade_path))

    src, is_stream = open_source(args.source)

    writer = None
    if args.write and is_stream:
        # Preparar writer de vídeo (mismo tamaño que la fuente)
        ret, frame = src.read()
        if not ret:
            print("[ERROR] No se pudo leer el primer frame para inicializar el writer.")
            sys.exit(1)
        h, w = frame.shape[:2]
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter(args.write, fourcc, max(24, int(src.get(cv2.CAP_PROP_FPS) or 24)), (w, h))
        src.set(cv2.CAP_PROP_POS_FRAMES, 0)  # reiniciar

    def process_frame(frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if args.gray_eq:
            gray = cv2.equalizeHist(gray)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=args.scale_factor,
            minNeighbors=args.min_neighbors,
            minSize=(args.min_size, args.min_size),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        # Dibujar
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Face", (x, y - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 1, cv2.LINE_AA)
        # Contador
        cv2.putText(frame, f"Detections: {len(faces)}", (10, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (20, 20, 20), 2, cv2.LINE_AA)
        cv2.putText(frame, f"Detections: {len(faces)}", (10, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (240, 240, 240), 1, cv2.LINE_AA)
        return frame

    if is_stream:
        # Bucle para webcam o vídeo
        while True:
            ret, frame = src.read()
            if not ret:
                break
            out = process_frame(frame)

            if writer is not None:
                writer.write(out)

            # Mostrar si se pide o si la fuente es webcam
            if args.display or (args.source.isdigit()):
                cv2.imshow("Haar Face Detection", out)
                if cv2.waitKey(1) & 0xFF in (27, ord('q')):  # ESC o q
                    break

        if writer is not None:
            writer.release()
        if hasattr(src, "release"):
            src.release()
        cv2.destroyAllWindows()
    else:
        # Fuente es imagen
        out = process_frame(src)
        if args.write:
            # Guardar como imagen si la salida termina en extensión de imagen
            out_path = Path(args.write)
            if out_path.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp"]:
                cv2.imwrite(str(out_path), out)
                print(f"[OK] Imagen guardada en: {out_path}")
            else:
                print("[ADVERTENCIA] --write apunta a un archivo no-imagen. Ignorando guardado para imagen fija.")
        if args.display or True:
            cv2.imshow("Haar Face Detection (Image)", out)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

if _name_ == "_main_":
    main()
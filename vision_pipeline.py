import cv2

def crop_minimap(video_path: str):
    """
    Lit une vidéo de replay et isole la minimap en bas à droite de l'écran.
    Paramétré pour une résolution standard de 1920x1080.
    """
    # Ouverture de la vidéo
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Erreur technique : Impossible de lire la vidéo {video_path}")
        return

    print("Appuie sur la touche 'q' pour quitter l'affichage.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Fin de la vidéo ou erreur de lecture.")
            break

        # Coordonnées approximatives de la minimap sur un écran 1920x1080
        # Format OpenCV : frame[y_start:y_end, x_start:x_end]
        # (À ajuster d'une centaine de pixels selon ton interface en jeu)
        y_start, y_end = 760, 1080
        x_start, x_end = 1600, 1920
        
        minimap_cropped = frame[y_start:y_end, x_start:x_end]

        # Affichage des fenêtres pour comparer
        cv2.imshow('1. Replay Complet', frame)
        cv2.imshow('2. Minimap Isolee (Pour YOLO)', minimap_cropped)

        # Quitter avec la touche 'q'
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Remplace 'replay.mp4' par le nom d'un petit clip vidéo dans ton dossier
    crop_minimap("replay.mp4")
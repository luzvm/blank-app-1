import streamlit as st
import cv2
import time

# Función para capturar video
def capture_video():
    cap = cv2.VideoCapture(0)  # Usa la cámara por defecto
    stframe = st.empty()  # Espacio vacío en Streamlit para mostrar los frames

    while True:
        ret, frame = cap.read()
        if not ret:
            st.write("No se pudo acceder a la cámara")
            break

        # Convertir a RGB para que Streamlit lo muestre correctamente
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Mostrar el frame
        stframe.image(frame_rgb, channels="RGB", use_column_width=True)

        # Esperar un breve momento para que no se congele
        time.sleep(0.01)

    cap.release()

# Configuración de la aplicación Streamlit
st.title("Aplicación de Cámara en Streamlit")

# Botón para abrir y cerrar la cámara
if st.button("Abrir/Cerrar Cámara"):
    capture_video()

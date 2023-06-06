import streamlit as st
import cv2
import numpy as np

def remove_background(image):
    # Converta a imagem para escala de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Aplique uma transformação para remover o fundo
    _, mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY_INV)
    
    # Aplique a máscara na imagem original
    result = cv2.bitwise_and(image, image, mask=mask)
    
    return result

def main():
    st.title("Removedor de Background")
    
    # Carregue a imagem
    uploaded_file = st.file_uploader("Selecione uma imagem", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Leia a imagem
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        
        # Redimensione a imagem para caber na tela
        max_width = 800
        if image.shape[1] > max_width:
            scale_factor = max_width / image.shape[1]
            image = cv2.resize(image, (max_width, int(image.shape[0] * scale_factor)))
        
        st.image(image, channels="BGR", caption="Imagem Original")
        
        # Remova o fundo da imagem
        result = remove_background(image)
        
        st.image(result, channels="BGR", caption="Imagem sem Background")

if __name__ == "__main__":
    main()

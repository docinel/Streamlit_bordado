import streamlit as st
import os

st.set_page_config(
    page_title="Bordado",
    page_icon="👋",
)

imagens = r'C:\Users\rodrigo.docinel\Documents\Streamlit_bordado\images'

st.markdown(
    """
    <style>
    .main {
        background-color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: white;'>Bordado</h1>", unsafe_allow_html=True)

# Listar os arquivos na pasta
arquivos = [arquivo for arquivo in os.listdir(imagens) if os.path.isfile(os.path.join(imagens, arquivo))]

# Selecionar o arquivo
arquivo_selecionado = st.selectbox("Selecione o arquivo:", arquivos)

# Carregar a imagem
imagem = os.path.join(imagens, arquivo_selecionado)
imagem = st.image(imagem, use_column_width=True)
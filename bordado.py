import streamlit as st
import os

st.set_page_config(
    page_title="Bordado",
    page_icon="👋",
)

# Acessar a pasta contendo as imagens
local = os.getcwd()

# Caminho para as imagens
images = os.path.join(local, 'images')


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
arquivos = os.listdir(images)

# Selecionar o arquivo
arquivo_selecionado = st.selectbox("Selecione o arquivo:", arquivos)

# Carregar a imagem
imagem = os.path.join(images, arquivo_selecionado)
imagem = st.image(imagem, use_column_width=True)
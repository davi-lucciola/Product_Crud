import streamlit as st
from db.crud import *


# Configurando Pagina
st.set_page_config(
    page_title='Cadastro',
    page_icon='✅'
)

# Main Page
'''
    # Inserir Novo Produto
'''

with st.form('Inserir'):
    nome = st.text_input('Nome do Produto')
    preco = st.number_input('Preço: ')
    button = st.form_submit_button('Cadastrar')

if button:
    if produtos_db.inserir(nome, preco):
        st.success('Produto Cadastrado com sucesso!')
    else:
        st.error('Não foi possivel cadastrar ao banco')
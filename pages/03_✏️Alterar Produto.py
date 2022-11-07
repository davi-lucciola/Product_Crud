import streamlit as st
from db.crud import *


# Configurando Pagina
st.set_page_config(
    page_title='Alterar',
    page_icon='✏️'
)

# Main Page
'''
# Alterar Produto Existente
'''

with st.form('Alterar'):
    id_prod = st.number_input('ID do Produto', min_value=0, step=1)
    novo_nome = st.text_input('Novo nome do Produto')
    novo_preco = st.number_input('Novo Preço')
    button = st.form_submit_button('Alterar')

if button:
    if produtos_db.alterar(id_prod, novo_nome, novo_preco):
        st.success('Produto Alterado com Sucesso!')
    else:
        st.error('Houve um Erro ao Alterar o Produto!')
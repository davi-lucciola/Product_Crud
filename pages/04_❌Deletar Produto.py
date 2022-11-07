import streamlit as st
from db.crud import *


# Configurando Pagina
st.set_page_config(
    page_title='Excluir',
    page_icon='❌'
)

# Main Page
'''
# Deletar Produto
'''

with st.form('Deletar'):
    id_prod = st.number_input('ID do Produto', min_value=0, step=1)
    button = st.form_submit_button('Deletar')

if button:
    if produtos_db.deletar(id_prod):
        st.success('Produto Deletado com Sucesso!')
    else:
        st.error('Houve um Erro ao Deletar o Produto!')
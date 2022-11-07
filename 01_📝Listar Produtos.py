import pandas as pd
import streamlit as st
from db.crud import *


# Configurando Pagina
st.set_page_config(
    page_title='Produtos',
    page_icon='📝'
)

# Main Page
'''
# Produtos Cadastrados
'''

produtos_cadastrados: pd.DataFrame = produtos_db.listar_todos()
st.dataframe(produtos_cadastrados, use_container_width=True)
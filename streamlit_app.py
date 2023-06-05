import streamlit as st
import pandas as pd
from datetime import datetime

def main():
    st.title('Sistema de Planner')

    task_name = st.text_input('Nome da tarefa')
    task_description = st.text_area('Descrição da tarefa')
    task_due_date = st.date_input('Data de vencimento')

    if st.button('Adicionar Tarefa'):
        st.success('Tarefa adicionada com sucesso!')
        # Adicionar a tarefa a um DataFrame ou banco de dados
        # Exemplo: df = pd.DataFrame([[task_name, task_description, task_due_date]], columns=['Nome', 'Descrição', 'Data de vencimento'])

if __name__ == '__main__':
    main()

import streamlit as st
import pandas as pd
import json
import os

def main():
    st.title('Sistema de Planner')

    # Verificar se o arquivo JSON existe
    if not os.path.exists('tasks.json'):
        with open('tasks.json', 'w') as file:
            json.dump([], file)

    tasks = load_tasks()

    menu_options = ['Visualizar Tarefas', 'Adicionar Tarefa']
    choice = st.sidebar.selectbox('Menu', menu_options)

    if choice == 'Visualizar Tarefas':
        view_tasks(tasks)
    elif choice == 'Adicionar Tarefa':
        add_task(tasks)

def view_tasks(tasks):
    if tasks:
        st.subheader('Tarefas:')
        df = pd.DataFrame(tasks)
        st.dataframe(df)
    else:
        st.info('Nenhuma tarefa adicionada ainda.')

def add_task(tasks):
    st.subheader('Adicionar Tarefa')
    task_name = st.text_input('Nome da tarefa')
    task_description = st.text_area('Descrição da tarefa')
    task_due_date = st.date_input('Data de vencimento')

    if st.button('Salvar Tarefa'):
        task = {
            'Nome': task_name,
            'Descrição': task_description,
            'Data de vencimento': str(task_due_date),
            'Finalizada': False
        }

        tasks.append(task)
        save_tasks(tasks)
        st.success('Tarefa adicionada com sucesso!')

def load_tasks():
    with open('tasks.json', 'r') as file:
        try:
            tasks = json.load(file)
        except json.JSONDecodeError:
            tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

if __name__ == '__main__':
    main()

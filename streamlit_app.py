import streamlit as st
import pandas as pd
import json
import os

def main():
    st.title('Sistema de Planner')

    # Tela de login
    if not is_user_logged_in():
        login()

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

def login():
    st.subheader('Login')
    username = st.text_input('Usuário')
    password = st.text_input('Senha', type='password')
    if st.button('Entrar'):
        if authenticate(username, password):
            st.success('Login bem-sucedido!')
            set_user_logged_in(True)
        else:
            st.error('Usuário ou senha inválidos.')

def authenticate(username, password):
    # Verificar se o usuário e senha correspondem a algum perfil existente
    profiles = load_profiles()
    for profile in profiles:
        if profile['username'] == username and profile['password'] == password:
            return True
    return False

def set_user_logged_in(logged_in):
    # Salvar estado do login em um arquivo
    with open('login_status.json', 'w') as file:
        json.dump(logged_in, file)

def is_user_logged_in():
    # Verificar estado do login a partir do arquivo
    if not os.path.exists('login_status.json'):
        set_user_logged_in(False)  # Criar o arquivo se não existir
        return False
    with open('login_status.json', 'r') as file:
        logged_in = json.load(file)
    return logged_in

def view_tasks(tasks):
    if tasks:
        st.subheader('Tarefas:')
        df = pd.DataFrame(tasks)
        st.dataframe(df)

        task_index = st.selectbox('Selecione a tarefa', df.index)
        selected_task = tasks[task_index]

        if st.button('Finalizar Tarefa'):
            complete_task(selected_task)
            st.success('Tarefa finalizada com sucesso!')

        if st.button('Excluir Tarefa'):
            delete_task(tasks, task_index)
            st.success('Tarefa excluída com sucesso!')
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

def complete_task(task):
    task['Finalizada'] = True
    save_tasks(tasks)

def delete_task(tasks, index):
    tasks.pop(index)
    save_tasks(tasks)

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

def load_profiles():
    try:
        with open('profiles.json', 'r') as file:
            profiles = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        profiles = []
    return profiles

if __name__ == '__main__':
    main()

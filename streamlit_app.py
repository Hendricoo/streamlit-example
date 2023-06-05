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

    if st.button('Adicionar Tarefa'):
        task_name = st.text_input('Nome da tarefa')
        task_description = st.text_area('Descrição da tarefa')
        task_due_date = st.date_input('Data de vencimento')

        task = {
            'Nome': task_name,
            'Descrição': task_description,
            'Data de vencimento': str(task_due_date),
            'Finalizada': False
        }

        tasks.append(task)
        save_tasks(tasks)
        st.success('Tarefa adicionada com sucesso!')

    if tasks:
        st.subheader('Tarefas:')
        df = pd.DataFrame(tasks)
        st.dataframe(df)

        task_index = st.selectbox('Selecione a tarefa', df.index)
        selected_task = tasks[task_index]

        if st.button('Editar Tarefa'):
            edit_task(selected_task)

        if selected_task['Finalizada']:
            st.warning('Esta tarefa já foi finalizada!')
        else:
            if st.button('Finalizar Tarefa'):
                complete_task(selected_task)
                st.success('Tarefa finalizada com sucesso!')

        if st.button('Excluir Tarefa'):
            delete_task(tasks, task_index)
            st.success('Tarefa excluída com sucesso!')

    else:
        st.info('Nenhuma tarefa adicionada ainda.')

def edit_task(task):
    st.sidebar.subheader('Editar Tarefa')
    new_name = st.sidebar.text_input('Nome da tarefa', task['Nome'])
    new_description = st.sidebar.text_area('Descrição da tarefa', task['Descrição'])
    new_due_date = st.sidebar.date_input('Data de vencimento', pd.to_datetime(task['Data de vencimento']).date())

    task['Nome'] = new_name
    task['Descrição'] = new_description
    task['Data de vencimento'] = str(new_due_date)

    if st.sidebar.button('Atualizar Tarefa'):
        save_tasks(tasks)
        st.sidebar.success('Tarefa atualizada com sucesso!')

def complete_task(task):
    task['Finalizada'] = True
    save_tasks(tasks)

def delete_task(tasks, index):
    tasks.pop(index)
    save_tasks(tasks)

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

if __name__ == '__main__':
    main()

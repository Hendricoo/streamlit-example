import streamlit as st
import pandas as pd
import json

def main():
    st.title('Sistema de Planner')

    # Verificar se o arquivo JSON existe
    tasks = load_tasks()

    if st.button('Adicionar Tarefa'):
        task_name = st.text_input('Nome da tarefa')
        task_description = st.text_area('Descrição da tarefa')
        task_due_date = st.date_input('Data de vencimento')

        task = {
            'Nome': task_name,
            'Descrição': task_description,
            'Data de vencimento': str(task_due_date)
        }

        tasks.append(task)
        save_tasks(tasks)
        st.success('Tarefa adicionada com sucesso!')

    if tasks:
        st.subheader('Tarefas:')
        df = pd.DataFrame(tasks)
        st.dataframe(df)

        task_index = st.selectbox('Selecione a tarefa para editar', df.index)
        selected_task = tasks[task_index]

        new_name = st.text_input('Nome da tarefa', selected_task['Nome'])
        new_description = st.text_area('Descrição da tarefa', selected_task['Descrição'])
        new_due_date = st.date_input('Data de vencimento', pd.to_datetime(selected_task['Data de vencimento']).date())

        if st.button('Atualizar Tarefa'):
            tasks[task_index] = {
                'Nome': new_name,
                'Descrição': new_description,
                'Data de vencimento': str(new_due_date)
            }
            save_tasks(tasks)
            st.success('Tarefa atualizada com sucesso!')

    else:
        st.info('Nenhuma tarefa adicionada ainda.')

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

if __name__ == '__main__':
    main()

import streamlit as st
from json import loads
from pandas import read_csv

st.markdown('''
# Exibidor de arquivos

## Suba um arquivo e vejamos o que acontece :smile::heart:
''')

arquivo = st.file_uploader(
    'Suba seu arquivo aqui!',
    type=['jpg', 'png', 'py', 'wav', 'csv', 'json']
)

st.text_input('Email', max_chars=10)
st.text_input('Senha', type='password')

if arquivo:
    print(arquivo.type)
    arquivo_type = arquivo.type.split('/')
    
    if arquivo_type[0] == 'application' and arquivo_type[1] == 'json':
        st.json(loads(arquivo.read()))
    elif arquivo_type[0] == 'image':
        st.image(arquivo)
    elif arquivo_type[0] == 'text' and arquivo_type[1] == 'csv':
        df = read_csv(arquivo).transpose()
        st.dataframe(df)
        st.bar_chart(df)
    elif arquivo_type[0] == 'text' and arquivo_type[1] == 'x-python':
        st.code(arquivo.read().decode())
    elif arquivo_type[0] == 'audio':
        st.audio(arquivo)
else:
    st.error('Ainda não tenho arquivo!')

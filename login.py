import streamlit as st
import json
import login

if login == True:

    def main():
     st.title("Sistema de Login")

     profiles = load_profiles()

    # Verifica se há perfis salvos
     if not profiles:
          st.info("Nenhum perfil encontrado. Por favor, crie um novo perfil.")
          create_profile(profiles)
     else:
        # Tela de login
        st.subheader("Login")
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")

        if st.button("Entrar"):
            if authenticate(username, password, profiles):
                st.success("Login bem-sucedido!")
                show_profile(username, profiles)
            else:
                st.error("Usuário ou senha inválidos.")

        # Opção de criar novo perfil
        st.subheader("Criar Novo Perfil")
        create_profile(profiles)

def authenticate(username, password, profiles):
    for profile in profiles:
        if (
            profile["username"] == username
            and profile["password"] == password
        ):
            return True
    return False

def create_profile(profiles):
    st.write("Crie um novo perfil:")
    new_username = st.text_input("Usuário")
    new_password = st.text_input("Senha", type="password")
    if st.button("Criar Perfil"):
        if not profile_exists(new_username, profiles):
            profile = {"username": new_username, "password": new_password}
            profiles.append(profile)
            save_profiles(profiles)
            st.success("Perfil criado com sucesso!")
        else:
            st.error("O usuário já existe. Por favor, escolha outro nome de usuário.")

def show_profile(username, profiles):
    st.subheader(f"Perfil: {username}")
    st.write("Detalhes do perfil:")
    for profile in profiles:
        if profile["username"] == username:
            st.write(f"Usuário: {profile['username']}")
            st.write(f"Senha: {profile['password']}")
            break

def load_profiles():
    try:
        with open("profiles.json", "r") as file:
            profiles = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        profiles = []
    return profiles

def save_profiles(profiles):
    with open("profiles.json", "w") as file:
        json.dump(profiles, file, indent=4)

def profile_exists(username, profiles):
    for profile in profiles:
        if profile["username"] == username:
            return True
    return False

if __name__ == "__main__":
    main()
else:
   st. print("Faça login antes")
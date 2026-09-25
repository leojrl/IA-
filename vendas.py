# Autor: leonardo
# Projeto: Automação de Vendas com IA

# -------- Bibliotecas --------
import streamlit as st # pip install streamlit
import pandas as pd # pip install pandas
import json
from google import genai # pip install google-genai

# -------- Configurações --------
with open ("token.json") as arquivo:
    token = json.load(arquivo)

client = genai.Client(api_key=token["api_key"])

# -------- Interface --------
st.title("🤖 Agente de IA - Vendas")

# abrir uma planilha específica
arquivo = st.file_uploader(
    "Escolha a planilha",
    type=["xlsx"]
)

# condicional para ler os dados da planilha
if arquivo:
    dados = pd.read_excel(arquivo)
    st.subheader("Dados da planilha")
    st.dataframe(dados)
    pergunta = st.text_input("O que deseja saber?")


    if st.button ("pergunta!") and pergunta:
        contexto = dados.to_string(index=False)
        
        prompt = f"""
você é um agente de análise de vendas.
responda à pergunta usando somente os dados da plainilha abaixo.
planilha: {contexto}
pergunta; {pergunta}
responda de forma simples e direta. 
"""
        resposta = client.models.generate_content(
         model="gemini-3.5-flash-lite",
         contents=prompt    
        )
        st.subheader("resposta")
        st.write(resposta.text) 
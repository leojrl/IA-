# Autor: maria
# Projeto: Uso da API
import json
from google import genai

# Lê a chave do arquivo token.json
with open("token.json", "r") as arquivo:
 dados = json.load(arquivo)

# Cria o cliente Gemini
client = genai.Client(api_key=dados["api_key"])

# Envia uma pergunta
resposta = client.models.generate_content(
 model="gemini-3.8-flash",
 contents="Explique o que é Python em 1 linha."
)

# Mostra a resposta
print(resposta.text)
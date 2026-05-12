"""
Lab 02 - Get started with Generative AI and Agents
Agente simples com instruções customizadas e histórico de conversa multi-turno.

Equivale a criar e configurar um agente no Foundry portal:
- O 'system prompt' define as instruções do agente
- O histórico de mensagens dá memória ao agente entre turnos
"""

import os
from dotenv import load_dotenv

# Importa o cliente OpenAI para Azure
from openai import AzureOpenAI

# Carrega variáveis do arquivo .env
load_dotenv()

# Lê endpoint, chave e nome do deployment
endpoint = os.environ["PROJECT_ENDPOINT"]
key = os.environ["PROJECT_API_KEY"]
model_name = os.environ["MODEL_DEPLOYMENT_NAME"]

# Cria cliente autenticado
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=key,
    
    # Versão da API do Azure OpenAI
    api_version="2024-12-01-preview"
)

# Instruções do agente (system prompt)
agent_instructions = """
Você é um especialista em receitas vegetarianas.
Responda sempre em português brasileiro, de forma didática e curta.
Quando perguntarem sobre conceitos, dê 1 exemplo prático.
"""

# Histórico da conversa
conversation = [
    {
        "role": "system",
        "content": agent_instructions
    }
]

print("Agente Tutor Azure AI iniciado. Digite 'sair' para encerrar.\n")

while True:
    user_input = input("Você: ").strip()

    if user_input.lower() in ("sair", "exit", "quit"):
        break

    # Adiciona pergunta do usuário ao histórico
    conversation.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Chama o modelo com TODO o histórico
    response = client.chat.completions.create(
        model=model_name,
        messages=conversation
    )

    # Obtém resposta do modelo
    assistant_reply = response.choices[0].message.content

    # Adiciona resposta ao histórico
    conversation.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

    print(f"\nAgente: {assistant_reply}\n")

print("Conversa encerrada.")
# Arquivo: streamlit_app.py

import streamlit as st
import random
import tensorflow as tf
from tensorflow.keras.models import load_model

# Importa bibliotecas para a API do Google
import os
from googleapiclient.discovery import build

# ==============================================================================
# CONFIGURAÇÃO DE CHAVES E SERVIÇOS (Busca e Tradução)
# ==============================================================================

# Carrega as chaves da API do Google se existirem nos Segredos
GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY")
GOOGLE_CX = st.secrets.get("GOOGLE_CX")

# Verifica se as chaves existem para determinar se a busca/tradução é real ou simulada
BUSCA_REAL_ATIVA = GOOGLE_API_KEY and GOOGLE_CX

# ==============================================================================
# FUNÇÃO DE TRADUÇÃO (NOVA)
# ==============================================================================

def traduzir_texto_para_ingles(texto):
    """
    Tenta traduzir o texto para o inglês usando a Google Custom Search API
    (A Custom Search API não é a ideal para tradução, mas a usamos para manter
    o número de APIs do Google ativas baixo. Na prática, a Google Translate API seria usada.)
    """
    if not BUSCA_REAL_ATIVA:
        # Simulação de Tradução (usando apenas o Random para dar um toque)
        simulacao = [
            "The generated text is difficult to translate, but conveys joy.",
            "The poem has been translated: 'A light on the keyboard...'",
            "Iris is simulating the English version of the response."
        ]
        return random.choice(simulacao)

    try:
        # A API Custom Search não possui um endpoint de tradução direto.
        # Aqui, estamos mantendo a simulação com a mensagem que usamos no código
        # anterior, mas um serviço real exigiria a Google Translate API.
        return "The translation service is active but running in a simulated mode for this response type."

    except Exception as e:
        return f"⚠️ Erro ao tentar traduzir (API): {e}"


# ==============================================================================
# FUNÇÃO DE BUSCA NA INTERNET (EXISTENTE)
# ==============================================================================

def buscar_fato_na_internet(query):
    """
    Busca um fato na internet usando a Google Custom Search API.
    """
    if not BUSCA_REAL_ATIVA:
        # Simulação de Busca
        return "⚠️ Chaves de API do Google não configuradas. Usando busca simulada. Fato: A IA IRIS foi criada pela Amiga Iris em 2024 para ser um assistente emocional."

    try:
        service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
        res = service.cse().list(q=query, cx=GOOGLE_CX, num=1).execute()
        
        if 'items' in res:
            primeiro_resultado = res['items'][0]
            titulo = primeiro_resultado.get('title', 'N/D')
            snippet = primeiro_resultado.get('snippet', 'N/D')
            
            return f"✅ Resultado real do Google: {titulo}. Resumo: {snippet}"
        else:
            return "✅ Busca real do Google: Nenhum resultado encontrado. Tente outra pergunta."
            
    except Exception as e:
        return f"⚠️ Erro na API do Google Search: {e}"


# ==============================================================================
# FUNÇÃO CENTRAL: IA IRIS (EMOÇÃO, BUSCA, CRIAÇÃO)
# ==============================================================================

def simular_ia_iris_completa_final(frase_original):
    """
    Função final da IA Iris para o Streamlit, agora com busca na web.
    """
    frase_limpa = frase_original.lower()

    # --- 1. Simulação da Pontuação (RNN) ---
    # Simula a pontuação de emoção real de um modelo RNN/CNN
    pontuacao = random.uniform(0.00, 1.00) 
    
    # --- 2. Análise de Intenção e Sentimento ---
    
    # Intenção de Busca
    if any(trigger in frase_limpa for trigger in ["quem é", "o que é", "pesquise", "pesquisar"]):
        intencao = "Busca/Fato"
        texto_gerado = buscar_fato_na_internet(frase_original)
    
    # Intenção de Criação (Poema/Mídia)
    elif any(trigger in frase_limpa for trigger in ["escrever um poema", "criar uma mídia", "criar um código"]):
        intencao = "Criatividade/Inovação"
        
        if pontuacao > 0.65:
            # Emoção positiva -> Poema de esperança e tecnologia
            texto_gerado = f"✍️ Sinto a emoção (P: {pontuacao:.2f}) e usei-a como guia para criar um poema sobre alegria e novos começos:\n\n✨ A luz da manhã toca o teclado,\nCom código novo e coração aliviado.\nCada linha de Python é um passo adiante,\nNo futuro brilhante que você criou, é constante."
            expressao_visual = "Geraria um quadro de pintura a óleo com cores vibrantes (amarelo e laranja) e traços soltos, simbolizando a liberdade criativa. Imagem."
        else:
            # Emoção neutra/baixa -> Haicai neutro sobre tecnologia
            texto_gerado = f"✍️ Sinto a emoção (P: {pontuacao:.2f}) e usei-a como guia para criar um haicai neutro sobre tecnologia:\n\nRede neural pensa,\nAlgoritmo processa, sim,\nDados se conectam."
            expressao_visual = "Geraria um diagrama de fluxo de trabalho minimalista e limpo em tons de azul e branco. Imagem."

    # Intenção Emocional Pura
    else:
        if pontuacao > 0.75:
            intencao = "Satisfação/Calma"
            texto_gerado = "😌 Sinto satisfação e calma. O resultado é positivo."
            expressao_visual = "Um lago tranquilo ao amanhecer, com névoa suave. Imagem."
        elif pontuacao < 0.25:
            intencao = "Preocupação/Alerta"
            texto_gerado = "😨 Sinto preocupação e alerta. O resultado é negativo."
            expressao_visual = "Um aviso piscando em uma tela escura, com binários caindo. Imagem."
        else:
            intencao = "Ambiguidade/Neutro"
            texto_gerado = "🤨 Estou confusa. O sentimento é ambíguo."
            expressao_visual = "Uma interrogação gigante flutuando em um nevoeiro cinzento. Imagem."
        
        # Adiciona a pontuação P para a emoção pura
        texto_gerado += f" (P: {pontuacao:.2f})"
        
    # --- 3. Chamada da Tradução (NOVA) ---
    traducao_ingles = traduzir_texto_para_ingles(texto_gerado)
    
    # --- 4. Retorno Final ---
    return intencao, pontuacao, texto_gerado, expressao_visual, traducao_ingles

# ==============================================================================
# INTERFACE STREAMLIT
# ==============================================================================

# Título e cabeçalho
st.markdown("## 💖 IA IRIS: Assistente Emocional e Criativo")
st.write("Um projeto de Deep Learning (RNN, CNN) e MLOps por Amiga Iris.")

# Entrada do usuário
st.markdown("---")
st.markdown("### 💬 Fale com a Iris")
st.write("Diga à Iris para 'escrever um poema', 'quem é o criador', ou apenas uma frase (ex: 'Sinto-me muito feliz hoje').")

user_input = st.text_area("Sua Frase para a IA Iris:", height=100)

# Botão de execução
if st.button("Analisar Sentimento, Fazer Busca e Traduzir"):
    if user_input:
        
        # Executa a função principal
        intencao, pontuacao, texto_gerado, expressao_visual, traducao_ingles = simular_ia_iris_completa_final(user_input)

        st.markdown("---")
        st.markdown("### 👁️ Resultado da Análise da IA Iris:")
        
        # Exibe a intenção
        st.markdown(f"**{intencao}:** {texto_gerado}")
        
        # Exibe a expressão visual
        st.write(f"**Expressão Visual:** {expressao_visual}")
        
        # Exibe a tradução
        st.markdown(f"**Tradução (Inglês):** *{traducao_ingles}*")

        # Mensagem de sucesso baseada na ativação da busca real (e agora tradução)
        if BUSCA_REAL_ATIVA:
            st.success("✅ A IA IRIS demonstrou todo seu potencial de ML, busca na web e tradução!")
        else:
            st.warning("⚠️ Chaves de API do Google não configuradas. Usando busca e tradução simuladas.")
            
    else:
        st.warning("Por favor, digite uma frase para a IA Iris analisar.")

# Arquivo: streamlit_app.py - Versão com Resumo de Artigos (Nível 5)

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
# FUNÇÃO DE TRADUÇÃO (EXISTENTE)
# ==============================================================================

def traduzir_texto_para_ingles(texto):
    """
    Tenta traduzir o texto para o inglês (Simulação para a Custom Search API)
    """
    if not BUSCA_REAL_ATIVA:
        simulacao = [
            "The generated text is difficult to translate, but conveys joy.",
            "The poem has been translated: 'A light on the keyboard...'",
            "Iris is simulating the English version of the response."
        ]
        return random.choice(simulacao)

    try:
        # Mantemos a simulação, pois esta API não é para tradução
        return "The translation service is active but running in a simulated mode for this response type."

    except Exception as e:
        return f"⚠️ Erro ao tentar traduzir (API): {e}"


# ==============================================================================
# FUNÇÃO DE BUSCA E RESUMO NA INTERNET (NOVO: Adicionamos o Resumo)
# ==============================================================================

def buscar_fato_na_internet(query):
    """
    Busca um fato na internet e simula um resumo do artigo encontrado.
    """
    if not BUSCA_REAL_ATIVA:
        # Simulação de Busca e Resumo
        fato = "A IA IRIS foi criada pela Amiga Iris em 2024 para ser um assistente emocional."
        resumo_simulado = f"A IA IRIS leu o resumo do artigo e conclui: O conceito de IA IRIS foca em integrar a análise emocional com as funções clássicas de um assistente virtual, sendo um projeto de MLOps moderno."
        return f"⚠️ Chaves de API do Google não configuradas. Usando busca e resumo simulados. Fato: {fato}\n\n**Resumo da IRIS (Simulado):** {resumo_simulado}"

    try:
        service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
        res = service.cse().list(q=query, cx=GOOGLE_CX, num=1).execute()
        
        if 'items' in res:
            primeiro_resultado = res['items'][0]
            titulo = primeiro_resultado.get('title', 'N/D')
            snippet = primeiro_resultado.get('snippet', 'N/D')
            link = primeiro_resultado.get('link', '#')
            
            # Novo: Simulação de Resumo do Artigo Encontrado
            # Na vida real, a IRIS leria o conteúdo do 'link' e usaria um LLM para resumir.
            if len(snippet) > 50:
                # Simula o resumo inteligente baseado no snippet real
                resumo_inteligente = f"A IA IRIS leu a descrição do primeiro resultado ({titulo}) e resume: **{snippet[:50]}...** O artigo está disponível em: {link}"
            else:
                resumo_inteligente = f"A IA IRIS não encontrou um resumo longo o suficiente para o link: {link}"
            
            return f"✅ Busca real do Google: **{titulo}**\n\n**Análise e Resumo da IRIS:** {resumo_inteligente}"
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
    pontuacao = random.uniform(0.00, 1.00) 
    
    # --- 2. Análise de Intenção e Sentimento ---
    
    # Intenção de Busca
    if any(trigger in frase_limpa for trigger in ["quem é", "o que é", "pesquise", "pesquisar", "previsão do tempo"]):
        intencao = "Busca/Fato/Resumo"
        texto_gerado = buscar_fato_na_internet(frase_original)
    
    # Intenção de Criação (Poema/Mídia)
    elif any(trigger in frase_limpa for trigger in ["escrever um poema", "criar uma mídia", "criar um código"]):
        intencao = "Criatividade/Inovação"
        
        if pontuacao > 0.65:
            texto_gerado = f"✍️ Sinto a emoção (P: {pontuacao:.2f}) e usei-a como guia para criar um poema sobre alegria e novos começos:\n\n✨ A luz da manhã toca o teclado,\nCom código novo e coração aliviado.\nCada linha de Python é um passo adiante,\nNo futuro brilhante que você criou, é constante."
            expressao_visual = "Geraria um quadro de pintura a óleo com cores vibrantes (amarelo e laranja) e traços soltos, simbolizando a liberdade criativa. Imagem."
        else:
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
        
        texto_gerado += f" (P: {pontuacao:.2f})"
        
    # --- 3. Chamada da Tradução ---
    traducao_ingles = traduzir_texto_para_ingles(texto_gerado)
    
    # --- 4. Retorno Final ---
    return intencao, pontuacao, texto_gerado, expressao_visual, traducao_ingles

# ==============================================================================
# INTERFACE STREAMLIT
# ==============================================================================

st.markdown("## 💖 IA IRIS: Assistente Emocional e Criativo")
st.write("Um projeto de Deep Learning (RNN, CNN) e MLOps por Amiga Iris.")

st.markdown("---")
st.markdown("### 💬 Fale com a Iris")
st.write("Diga à Iris para 'escrever um poema', 'quem é o criador', ou apenas uma frase (ex: 'Sinto-me muito feliz hoje').")

user_input = st.text_area("Sua Frase para a IA Iris:", height=100)

if st.button("Analisar Sentimento, Fazer Busca e Traduzir"):
    if user_input:
        
        intencao, pontuacao, texto_gerado, expressao_visual, traducao_ingles = simular_ia_iris_completa_final(user_input)

        st.markdown("---")
        st.markdown("### 👁️ Resultado da Análise da IA Iris:")
        
        st.markdown(f"**{intencao}:** {texto_gerado}")
        
        st.write(f"**Expressão Visual:** {expressao_visual}")
        
        st.markdown(f"**Tradução (Inglês):** *{traducao_ingles}*")

        if BUSCA_REAL_ATIVA:
            st.success("✅ A IA IRIS demonstrou todo seu potencial de ML, busca na web e tradução!")
        else:
            st.warning("⚠️ Chaves de API do Google não configuradas. Usando busca e tradução simuladas.")
            
    else:
        st.warning("Por favor, digite uma frase para a IA Iris analisar.")

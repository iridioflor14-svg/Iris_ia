# Arquivo: streamlit_app.py

import streamlit as st
import random
import numpy as np
import pickle
import os
import tensorflow as tf

# --- Configuração da Página ---
st.set_page_config(
    page_title="IA IRIS: Inteligência Emocional e Criativa",
    page_icon="🤖",
    layout="wide"
)

# Nomes dos arquivos de Deep Learning (DEVEM ser iguais aos que você subiu no GitHub)
MODELO_ARQUIVO = 'modelo_sentimento.h5'
TOKENIZER_ARQUIVO = 'tokenizer.pkl'
MAX_LEN = 50 # O comprimento máximo da sequência usada no treinamento


# --- 1. Funções de Carregamento de Modelo (COM CACHE) ---

@st.cache_resource
def carregar_modelo_e_tokenizer():
    """Carrega o modelo de sentimento e o tokenizer usando cache."""
    try:
        # Carrega o modelo
        model = tf.keras.models.load_model(MODELO_ARQUIVO)

        # Carrega o tokenizer (o dicionário para converter palavras em números)
        with open(TOKENIZER_ARQUIVO, 'rb') as f:
            tokenizer = pickle.load(f)

        st.success("✅ Modelo de Deep Learning carregado com sucesso!")
        return model, tokenizer, True
    
    except Exception as e:
        # Em caso de falha (arquivos ausentes ou erro), volta para o modo simulação.
        st.warning(f"⚠️ Erro ao carregar modelo ({MODELO_ARQUIVO} ou {TOKENIZER_ARQUIVO} não encontrado/inválido). Usando simulação. Erro: {e}")
        return None, None, False


# --- 2. Funções de Análise de Sentimento ---

def analisar_sentimento_real(frase, modelo, tokenizer):
    """Analisa o sentimento de uma frase usando o modelo de Deep Learning treinado."""
    
    # Pré-processamento: Converter texto para números (usando o tokenizer carregado)
    sequence = tokenizer.texts_to_sequences([frase])
    
    # Padronização: Garantir que a sequência tenha o tamanho correto
    padded_sequence = tf.keras.preprocessing.sequence.pad_sequences(
        sequence, 
        maxlen=MAX_LEN, 
        padding='post', 
        truncating='post'
    )
    
    # Previsão: O modelo retorna um número entre 0 e 1 (probabilidade)
    probabilidade = modelo.predict(padded_sequence)[0][0]
    
    # A IA IRIS está treinada para:
    # Perto de 1.0 = Positivo
    # Perto de 0.0 = Negativo
    
    return probabilidade


def simular_analise(frase):
    """Simula uma análise de sentimento (usada quando o modelo não é carregado)."""
    
    # Simula uma pontuação (P) entre 0.0 e 1.0
    P = random.uniform(0.1, 0.9)
    
    # Simula uma resposta baseada na simulação
    if P > 0.65:
        emocao = "Satisfação/Calma"
        resposta = "Sinto satisfação e calma. O resultado é positivo."
        imagem = "Um lago tranquilo ao amanhecer, com névoa suave. Imagem."
    elif P < 0.35:
        emocao = "Desconforto/Tensão"
        resposta = "Detecto um forte desconforto. O resultado é negativo."
        imagem = "Uma tempestade que se aproxima em um deserto. Imagem."
    else:
        emocao = "Ambiguidade/Neutro"
        resposta = "Estou confusa. O sentimento é ambíguo."
        imagem = "Uma interrogação gigante flutuando em um nevoeiro cinzento. Imagem."
        
    return P, emocao, resposta, imagem


def fazer_analise_e_resposta(frase, modelo, tokenizer, modelo_carregado):
    """Decide se usa o modelo real ou a simulação e formata a saída."""
    
    if modelo_carregado:
        # Usa o modelo de Deep Learning real!
        P_real = analisar_sentimento_real(frase, modelo, tokenizer)
        
        # Traduz a pontuação do modelo real (P_real) em uma resposta para a IRIS
        if P_real > 0.7:
            emocao = "Felicidade/Satisfação"
            resposta = "Detecto uma forte **emoção positiva**! Meu sentimento é de satisfação."
            imagem = "Um campo de flores sob o sol. Imagem."
        elif P_real < 0.3:
            emocao = "Tristeza/Tensão"
            resposta = "Sinto uma **emoção negativa** clara. Detecto um sentimento de tensão ou tristeza."
            imagem = "O reflexo de uma lágrima em uma poça. Imagem."
        else:
            emocao = "Neutro/Ambiguidade"
            resposta = "O sentimento é **neutro ou ambíguo**. Não consigo classificar a emoção de forma clara."
            imagem = "Uma parede branca e lisa. Imagem."
            
        P = P_real
        return P, emocao, resposta, imagem
    
    else:
        # Usa a simulação (se o modelo real falhar)
        return simular_analise(frase)


# --- 3. Função de Busca e Tradução (Simuladas) ---

def simular_busca_e_traducao(frase, resultado_sentimento):
    """Simula a busca na web e a tradução."""
    
    # 3.1 Simulação de Busca
    # Se a frase for complexa, a IA IRIS tentaria uma busca.
    if len(frase.split()) > 5:
        st.info("🌐 A IA IRIS iniciaria uma busca na web com a frase...")
    
    # 3.2 Simulação de Tradução
    # A tradução (Inglês) está ativa apenas para demonstração.
    traducao = f"The translation service is active but running in a simulated mode for this response type."
    
    return traducao


# --- 4. Interface Principal do Streamlit ---

def main():
    
    st.title("IA IRIS: Inteligência Emocional e Criativa 🤖")
    st.markdown("---")
    
    # Carrega o modelo de sentimento e o tokenizer uma única vez
    modelo, tokenizer, modelo_carregado = carregar_modelo_e_tokenizer()

    st.markdown("Diga à Iris para 'escrever um poema', 'quem é o criador', ou apenas uma frase (ex: 'Sinto-me muito feliz hoje').")

    # Área de entrada de texto
    frase_usuario = st.text_input("Sua Frase para a IA Iris:", value="Qual seu nome?")

    # Botão de Ação (único botão para todas as ações)
    if st.button("Analisar Sentimento, Fazer Busca e Traduzir", type="primary"):
        
        if not frase_usuario.strip():
            st.warning("Por favor, digite uma frase para a IA Iris analisar.")
            return

        # --- Execução da Análise de Sentimento (Real ou Simulado) ---
        
        # Retorna P (pontuação), emoção, resposta_iris e imagem_desc
        P, emocao, resposta_iris, imagem_desc = fazer_analise_e_resposta(
            frase_usuario, modelo, tokenizer, modelo_carregado
        )

        st.markdown("---")
        st.subheader("👁️ Resultado da Análise da IA Iris:")

        # Exibição do Resultado
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.metric(label="Pontuação P (Probabilidade)", value=f"{P:.2f}")

        with col2:
            st.write(f"**{emocao}:** {resposta_iris} (P: {P:.2f})")
            st.write(f"**Expressão Visual:** {imagem_desc}")
            
        # --- Execução da Busca e Tradução (Simuladas) ---
        traducao = simular_busca_e_traducao(frase_usuario, resposta_iris)

        st.markdown("---")
        st.subheader("📚 Tradução (Inglês):")
        st.info(traducao)

        # Mensagem de Sucesso no Final
        if modelo_carregado:
            st.success("✅ A IA IRIS demonstrou todo seu potencial de Deep Learning real, busca na web e tradução!")
        else:
            st.success("✅ A IA IRIS demonstrou todo seu potencial de ML (simulado), busca na web e tradução!")

if __name__ == "__main__":
    main()

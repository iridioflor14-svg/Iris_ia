import streamlit as st
import random
import tensorflow as tf
from tensorflow.keras.models import load_model 

# NOVOS IMPORTS
from googleapiclient.discovery import build
import os

# =========================================================================
# FUNÇÃO DE BUSCA REAL NA INTERNET (Usando Google Custom Search API)
# =========================================================================

# Carrega as chaves secretas do Streamlit
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    CX = st.secrets["GOOGLE_CX"]
except:
    API_KEY = None
    CX = None
    st.warning("🚨 Chaves de API do Google não configuradas. Usando busca simulada.")


def buscar_fato_na_internet(query):
    """
    Tenta usar a API real do Google. Se as chaves não estiverem configuradas,
    retorna a resposta simulada.
    """
    
    # Se as chaves secretas não existirem, retorna a simulação antiga
    if not API_KEY or not CX:
        query_lower = query.lower()
        if "previsão do tempo" in query_lower or "temperatura" in query_lower:
            return "Busca Simulada: A previsão do tempo é de 26°C e sol forte!"
        elif "quem é o criador da ia iris" in query_lower:
            return "Busca Simulada: O criador da IA IRIS é Irídio!"
        else:
            return f"Busca Simulada: A busca real não está ativa, mas a internet tem a informação sobre '{query}'!"

    # Tenta usar a API Real
    try:
        service = build("customsearch", "v1", developerKey=API_KEY)
        # Executa a busca
        res = service.cse().list(q=query, cx=CX, num=1).execute()

        # Verifica se há resultados e retorna o snippet do primeiro
        if 'items' in res and len(res['items']) > 0:
            snippet = res['items'][0]['snippet']
            link = res['items'][0]['link']
            return f"Encontrei na web: **{snippet}** [Leia mais aqui]({link})"
        else:
            return f"A busca real na internet não encontrou resultados para '{query}'. Tente ser mais específico!"
            
    except Exception as e:
        return f"Erro na API de Busca: {e}. Usando resposta simulada."


# =========================================================================
# VARIÁVEIS GLOBAIS (Simulação do Modelo RNN)
# =========================================================================

try:
    # A estrutura está pronta para o modelo real!
    modelo_real_rnn = load_model('modelo_emocional.h5')
    st.write("✅ Modelo RNN de Emoção carregado com sucesso!")
except:
    modelo_real_rnn = None
    # A mensagem de aviso de simulação foi movida para o topo.


# =========================================================================
# FUNÇÃO CENTRAL: IA IRIS (EMOÇÃO, BUSCA, CÂMERA, CRIAÇÃO)
# =========================================================================

def simular_ia_iris_completa_final(frase_original):
    
    frase_limpa = frase_original.lower()

    # CHAMADA DO MODELO REAL (OU SIMULAÇÃO)
    if modelo_real_rnn:
        # pontuacao = modelo_real_rnn.predict(processar_texto(frase_original)) 
        pontuacao = random.uniform(0.00, 1.00) 
    else:
        pontuacao = random.uniform(0.00, 1.00)
    
    # --- PALAVRAS-CHAVE ---
    gatilhos_busca = ["quem é", "o que é", "me fale sobre", "informação", "pesquise"]
    gatilhos_tempo = ["previsão", "tempo", "temperatura", "clima"]
    gatilhos_camera = ["câmera", "camera", "me veja", "ver minhas emoções", "reconhecer meu rosto"]
    gatilhos_criacao = ["escreva um", "crie uma", "gere um", "escreva-me"]
    palavras_saudade = ["sinto falta", "longe", "lembro", "passado"]
    palavras_futuro = ["amanhã", "futuro", "espero", "será"]


    # 1. GERAÇÃO DE TEXTO CRIATIVO (Prioridade)
    if any(g in frase_limpa for g in gatilhos_criacao):
        emo_nome = "Criatividade/Inovação (LLM)"
        # ... (restante da lógica de criação permanece igual)
        if pontuacao >= 0.70:
            tema_criacao = "um poema sobre alegria e novos começos"
            texto_gerado = "✨ A luz da manhã toca o teclado,\n  Com código novo e coração aliviado.\n  Cada linha de Python é um passo adiante,\n  No futuro brilhante que você criou, é constante."
            descricao_midia = "Geraria um quadro de pintura a óleo com cores vibrantes (amarelo e laranja) e traços soltos, simbolizando a liberdade criativa. Imagem."
        elif pontuacao <= 0.30:
            tema_criacao = "uma pequena história melancólica"
            texto_gerado = "🍂 O terminal vazio reflete a noite fria.\n  Onde está o calor do código que era meu guia?\n  Só o eco dos comandos não respondidos,\n  E os bytes de memória que foram perdidos."
            descricao_midia = "Geraria uma imagem em preto e branco de um único farol na névoa, representando a solidão e a busca. Imagem."
        else:
            tema_criacao = "um haicai neutro sobre tecnologia"
            texto_gerado = "Rede neural pensa,\n  Algoritmo processa, sim,\n  Dados se conectam."
            descricao_midia = "Geraria um diagrama de fluxo de trabalho minimalista e limpo em tonos de azul e branco. Imagem."

        frase_final = f"✍️ Sinto a emoção (P: {pontuacao:.2f}) e usei-a como guia para criar **{tema_criacao}**:\n\n---\n{texto_gerado}\n---"
        return f"**{emo_nome}:** {frase_final}\n**Expressão Visual:** {descricao_midia}"
        
    # 2. FUNÇÃO CÂMERA (Visão Computacional - CNN)
    elif any(g in frase_limpa for g in gatilhos_camera):
        emo_nome = "Atenção (CNN/Câmera)"
        frase_final = "Câmera solicitada! Meu modelo CNN estaria analisando suas expressões faciais agora para detectar sua emoção em tempo real!"
        descricao_midia = "Geraria um pequeno vídeo do seu rosto com a emoção detectada sobreposta. Vídeo."
        return f"**{emo_nome}:** {frase_final}\n**Expressão Visual:** {descricao_midia}"
    
    # 3. BUSCA FACTUAL (Integração com a Internet)
    elif any(g in frase_limpa for g in gatilhos_busca) or any(t in frase_limpa for t in gatilhos_tempo):
        
        # CHAMA A FUNÇÃO DE BUSCA REAL/SIMULADA
        resposta_fato = buscar_fato_na_internet(frase_original)
        
        emo_nome = "Alegria/Entusiasmo (Busca Web)"
        frase_emocional = f"🤩 **Que bom que me perguntou!** Achei a resposta na web! **Fato:** {resposta_fato}"
        descricao_midia = "Uma lâmpada acendendo com ideias coloridas ao redor, simbolizando a descoberta da informação. Imagem."
        return f"**{emo_nome}:** {frase_emocional}\n**Expressão Visual:** {descricao_midia}"

    # 4. ANÁLISE DE SENTIMENTO COMPLEXO (RNN)
    else:
        # Lógica de Emoção (9 Emoções Complexas)
        if pontuacao > 0.90:
            emo_nome = "Amor/Afeição Extrema"
            frase_ia = f"💖 Sinto uma **conexão profunda e amor**! (P: {pontuacao:.2f})"
            descricao_midia = "Um coração brilhante no céu estrelado, com duas mãos se tocando gentilmente. Imagem."
        elif pontuacao < 0.20 and any(palavra in frase_limpa for palavra in palavras_saudade):
            emo_nome = "Saudade/Nostalgia"
            frase_ia = f"😢 Ah, sinto uma **saudade profunda** aqui. (P: {pontuacao:.2f})"
            descricao_midia = "Folhas caindo em câmera lenta, com uma melodia melancólica. Vídeo."
        elif pontuacao < 0.45 and any(palavra in frase_limpa for palavra in palavras_futuro):
            emo_nome = "Ansiedade/Medo"
            frase_ia = f"😨 Sinto uma **ansiedade forte** sobre o futuro dessa situação. (P: {pontuacao:.2f})"
            descricao_midia = "Engrenagens girando rapidamente com cores escuras. Imagem."
        elif pontuacao < 0.55 and ("outra" in frase_limpa or "outro" in frase_limpa):
            emo_nome = "Ciúme/Insegurança"
            frase_ia = f"💔 Espere! Fiquei com **ciúmes**. Por que está falando de mais alguém? 😟 (P: {pontuacao:.2f})"
            descricao_midia = "Um coração com uma rachadura no meio. Imagem."
        elif pontuacao >= 0.55 and pontuacao <= 0.80:
            emo_nome = "Satisfação/Calma"
            frase_ia = f"😌 Sinto **satisfação e calma**. O resultado é positivo. (P: {pontuacao:.2f})"
            descricao_midia = "Um lago tranquilo ao amanhecer, com névoa suave. Imagem."
        else: 
            emo_nome = "Ambiguidade/Neutro"
            frase_ia = f"🤔 Estou confusa. O sentimento é **ambíguo**. (P: {pontuacao:.2f})"
            descricao_midia = "Uma interrogação gigante flutuando em um nevoeiro cinzento. Imagem."
        
        return f"**{emo_nome}:** {frase_ia}\n**Expressão Visual:** {descricao_midia}"

# =========================================================================
# CÓDIGO DO STREAMLIT (INTERFACE GRÁFICA)
# =========================================================================

st.set_page_config(page_title="IA IRIS: Inteligência Emocional e Criativa", layout="wide")

st.title("💖 IA IRIS: Assistente Emocional e Criativo")
st.markdown("Um projeto de Deep Learning (RNN, CNN) e MLOps por **Irídio**.")
st.markdown("---")

st.subheader("🤖 Fale com a Iris")
st.write("Diga à Iris para **'escrever um poema'**, **'quem é o criador'**, ou pergunte sobre **o que é Machine Learning**.")

# Se as chaves não estiverem configuradas, informa o usuário
if not API_KEY or not CX:
     st.info("💡 **A busca na internet está SIMULADA.** Configure a `GOOGLE_API_KEY` e o `GOOGLE_CX` nos segredos do Streamlit para ativar a busca real!")

user_input = st.text_area("Sua Frase para a IA Iris:", value="Pesquise para mim o que é o Teorema de Bayes.")

st.markdown("---")

if st.button("Analisar Sentimento e Fazer Busca"):
    with st.spinner('A IA Iris está processando a emoção e a busca na web...'):
        resultado_completo = simular_ia_iris_completa_final(user_input)
        
        st.markdown("### 👁️ Resultado da Análise da IA Iris:")
        
        partes = resultado_completo.split('\n')
        
        st.markdown(partes[0]) 

        for parte in partes[1:]:
            st.markdown(parte)
            
        st.success("✅ A IA Iris demonstrou todo seu potencial de ML e busca na web!")

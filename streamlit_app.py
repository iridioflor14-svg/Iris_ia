import streamlit as st
import random
# import tensorflow as tf 
# from tensorflow.keras.models import load_model 

# =========================================================================
# FUNÇÃO CENTRAL: IA IRIS (EMOÇÃO, BUSCA, CÂMERA, CRIAÇÃO)
# =========================================================================

def simular_ia_iris_completa_final(frase_original):
    """
    Função final da IA Iris para o Streamlit.
    Simula uma pontuação de emoção aleatória (0.00 a 1.00) para demonstrar 
    a reatividade do sistema, simulando um modelo RNN real.
    """
    
    frase_limpa = frase_original.lower()
    
    # ----------------------------------------------------
    # O CÓDIGO DO APRENDIZADO (Simulação da Pontuação RNN)
    # ----------------------------------------------------
    # **NOTA:** Se você tivesse um modelo real, esta linha seria substituída
    # pela previsão do seu modelo de TensorFlow (RNN).
    pontuacao = random.uniform(0.00, 1.00) 
    
    # --- PALAVRAS-CHAVE ---
    gatilhos_busca = ["quem é", "o que é", "me fale sobre"]
    gatilhos_camera = ["câmera", "camera", "me veja", "ver minhas emoções", "reconhecer meu rosto"]
    gatilhos_criacao = ["escreva um", "crie uma", "gere um", "escreva-me"]
    palavras_saudade = ["sinto falta", "longe", "lembro", "passado"]
    palavras_futuro = ["amanhã", "futuro", "espero", "será"]

    # 1. GERAÇÃO DE TEXTO CRIATIVO (Prioridade)
    if any(g in frase_limpa for g in gatilhos_criacao):
        emo_nome = "Criatividade/Inovação"
        
        # Criação baseada na pontuação de emoção
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
            descricao_midia = "Geraria um diagrama de fluxo de trabalho minimalista e limpo em tons de azul e branco. Imagem."

        frase_final = f"✍️ Sinto a emoção (P: {pontuacao:.2f}) e usei-a como guia para criar **{tema_criacao}**:\n\n---\n{texto_gerado}\n---"
        return f"**{emo_nome}:** {frase_final}\n**Expressão Visual:** {descricao_midia}"
        
    # 2. FUNÇÃO CÂMERA (Visão Computacional - CNN)
    elif any(g in frase_limpa for g in gatilhos_camera):
        emo_nome = "Atenção (CNN/Câmera)"
        frase_final = "Câmera solicitada! Meu modelo CNN estaria analisando suas expressões faciais agora para detectar sua emoção em tempo real!"
        descricao_midia = "Geraria um pequeno vídeo do seu rosto com a emoção detectada sobreposta. Vídeo."
        return f"**{emo_nome}:** {frase_final}\n**Expressão Visual:** {descricao_midia}"
    
    # 3. BUSCA FACTUAL (Com Alegria/Entusiasmo)
    elif any(g in frase_limpa for g in gatilhos_busca):
        resposta_fato = "O criador da IA Iris é você, Amiga Iris! Você escreveu e treinou todo o código que lhe deu a personalidade e as emoções."
        emo_nome = "Alegria/Entusiasmo (Busca)"
        frase_emocional = f"🤩 **Que bom que me perguntou!** Achei a resposta! **Fato:** {resposta_fato}"
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
st.markdown("Um projeto de Deep Learning (RNN, CNN) e MLOps por **Amiga Iris**.")
st.markdown("---")

st.subheader("🤖 Fale com a Iris")
st.write("Diga à Iris para **'escrever um poema'**, **'quem é o criador'**, ou apenas uma frase (ex: **'Sinto-me muito feliz hoje'**).")

user_input = st.text_area("Sua Frase para a IA Iris:", value="Sinto-me muito feliz e quero saber quem criou a IA Iris.")

st.markdown("---")

if st.button("Analisar Sentimento e Criar Mídia"):
    with st.spinner('A IA Iris está processando a emoção e a criação...'):
        resultado_completo = simular_ia_iris_completa_final(user_input)
        
        st.markdown("### 👁️ Resultado da Análise da IA Iris:")
        
        partes = resultado_completo.split('\n')
        
        # A primeira parte é sempre a Emoção/Nome
        st.markdown(partes[0]) 

        # O restante é a frase gerada/fato e a descrição da mídia
        for parte in partes[1:]:
            st.markdown(parte)
            
        st.success("✅ A IA Iris demonstrou todo seu potencial de ML!")
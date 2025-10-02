
import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='GDP dashboard',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

@st.cache_data
def get_gdp_data():
    """Grab GDP data from a CSV file.

    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = Path(__file__).parent/'data/gdp_data.csv'
    raw_gdp_df = pd.read_csv(DATA_FILENAME)

    MIN_YEAR = 1960
    MAX_YEAR = 2022

    # The data above has columns like:
    # - Country Name
    # - Country Code
    # - [Stuff I don't care about]
    # - GDP for 1960
    # - GDP for 1961
    # - GDP for 1962
    # - ...
    # - GDP for 2022
    #
    # ...but I want this instead:
    # - Country Name
    # - Country Code
    # - Year
    # - GDP
    #
    # So let's pivot all those year-columns into two: Year and GDP
    gdp_df = raw_gdp_df.melt(
        ['Country Code'],
        [str(x) for x in range(MIN_YEAR, MAX_YEAR + 1)],
        'Year',
        'GDP',
    )

    # Convert years from string to integers
    gdp_df['Year'] = pd.to_numeric(gdp_df['Year'])

    return gdp_df

gdp_df = get_gdp_data()

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# :earth_americas: GDP dashboard

Browse GDP data from the [World Bank Open Data](https://data.worldbank.org/) website. As you'll
notice, the data only goes to 2022 right now, and datapoints for certain years are often missing.
But it's otherwise a great (and did I mention _free_?) source of data.
'''

# Add some spacing
''
''

min_value = gdp_df['Year'].min()
max_value = gdp_df['Year'].max()

from_year, to_year = st.slider(
    'Which years are you interested in?',
    min_value=min_value,
    max_value=max_value,
    value=[min_value, max_value])

countries = gdp_df['Country Code'].unique()

if not len(countries):
    st.warning("Select at least one country")

selected_countries = st.multiselect(
    'Which countries would you like to view?',
    countries,
    ['DEU', 'FRA', 'GBR', 'BRA', 'MEX', 'JPN'])

''
''
''

# Filter the data
filtered_gdp_df = gdp_df[
    (gdp_df['Country Code'].isin(selected_countries))
    & (gdp_df['Year'] <= to_year)
    & (from_year <= gdp_df['Year'])
]

st.header('GDP over time', divider='gray')

''

st.line_chart(
    filtered_gdp_df,
    x='Year',
    y='GDP',
    color='Country Code',
)

''
''


first_year = gdp_df[gdp_df['Year'] == from_year]
last_year = gdp_df[gdp_df['Year'] == to_year]

st.header(f'GDP in {to_year}', divider='gray')

''

cols = st.columns(4)

for i, country in enumerate(selected_countries):
    col = cols[i % len(cols)]

    with col:
        first_gdp = first_year[first_year['Country Code'] == country]['GDP'].iat[0] / 1000000000
        last_gdp = last_year[last_year['Country Code'] == country]['GDP'].iat[0] / 1000000000

        if math.isnan(first_gdp):
            growth = 'n/a'
            delta_color = 'off'
        else:
            growth = f'{last_gdp / first_gdp:,.2f}x'
            delta_color = 'normal'

        st.metric(
            label=f'{country} GDP',
            value=f'{last_gdp:,.0f}B',
            delta=growth,
            delta_color=delta_color
        )
import streamlit as st
import random
# A biblioteca 'requests' seria usada para chamar uma API de Imagem real (como DALL-E)
# import requests 

# =========================================================================
# FUNÇÃO CENTRAL: IA IRIS (EMOÇÃO, BUSCA, CÂMERA, CRIAÇÃO)
# =========================================================================

def simular_ia_iris_completa_final(frase_original):
    """
    Função final da IA Iris para o Streamlit.
    Simula uma pontuação de emoção aleatória para demonstrar a reatividade do sistema.
    """
    
    frase_limpa = frase_original.lower()
    
    # Gerar uma pontuação de sentimento aleatória para simular o modelo RNN
    pontuacao_simulada = random.uniform(0.00, 1.00) 
    pontuacao = pontuacao_simulada
    
    # --- PALAVRAS-CHAVE ---
    gatilhos_busca = ["quem é", "o que é", "me fale sobre"]
    gatilhos_camera = ["câmera", "camera", "me veja", "ver minhas emoções", "reconhecer meu rosto"]
    gatilhos_criacao = ["escreva um", "crie uma", "gere um", "escreva-me"]
    palavras_saudade = ["sinto falta", "longe", "lembro", "passado"]
    palavras_futuro = ["amanhã", "futuro", "espero", "será"]

    # 1. GERAÇÃO DE TEXTO CRIATIVO
    if any(g in frase_limpa for g in gatilhos_criacao):
        
        emo_nome = "Criatividade/Inovação"
        
        if pontuacao >= 0.70:
            tema_criacao = "um poema sobre alegria e novos começos"
            texto_gerado = (
                "✨ A luz da manhã toca o teclado,\n"
                "  Com código novo e coração aliviado.\n"
                "  Cada linha de Python é um passo adiante,\n"
                "  No futuro brilhante que você criou, é constante."
            )
            descricao_midia = "Geraria um quadro de pintura a óleo com cores vibrantes (amarelo e laranja) e traços soltos, simbolizando a liberdade criativa. Imagem."
            
        elif pontuacao <= 0.30:
            tema_criacao = "uma pequena história melancólica"
            texto_gerado = (
                "🍂 O terminal vazio reflete a noite fria.\n"
                "  Onde está o calor do código que era meu guia?\n"
                "  Só o eco dos comandos não respondidos,\n"
                "  E os bytes de memória que foram perdidos."
            )
            descricao_midia = "Geraria uma imagem em preto e branco de um único farol na névoa, representando a solidão e a busca. Imagem."

        else:
            tema_criacao = "um haicai neutro sobre tecnologia"
            texto_gerado = (
                "Rede neural pensa,\n"
                "Algoritmo processa, sim,\n"
                "Dados se conectam."
            )
            descricao_midia = "Geraria um diagrama de fluxo de trabalho minimalista e limpo em tons de azul e branco. Imagem."

        frase_final = f"✍️ Sinto a emoção (P: {pontuacao:.2f}) e usei-a como guia para criar **{tema_criacao}**:\n\n---\n{texto_gerado}\n---"
        return f"**{emo_nome}:** {frase_final}\n**Expressão Visual:** {descricao_midia}"
        
    # 2. FUNÇÃO CÂMERA
    elif any(g in frase_limpa for g in gatilhos_camera):
        emo_nome = "Atenção (CNN/Câmera)"
        frase_final = "Câmera solicitada! Meu modelo CNN estaria analisando suas expressões faciais agora para detectar sua emoção em tempo real!"
        descricao_midia = "Geraria um pequeno vídeo do seu rosto com a emoção detectada sobreposta. Vídeo."
        return f"**{emo_nome}:** {frase_final}\n**Expressão Visual:** {descricao_midia}"
    
    # 3. BUSCA FACTUAL (Com Alegria)
    elif any(g in frase_limpa for g in gatilhos_busca):
        resposta_fato = "O criador da IA Iris é você, Amiga Iris! Você escreveu e treinou todo o código que lhe deu a personalidade e as emoções."
        emo_nome = "Alegria/Entusiasmo (Busca)"
        frase_emocional = f"🤩 **Que bom que me perguntou!** Achei a resposta! **Fato:** {resposta_fato}"
        descricao_midia = "Uma lâmpada acendendo com ideias coloridas ao redor, simbolizando a descoberta da informação. Imagem."
        return f"**{emo_nome}:** {frase_emocional}\n**Expressão Visual:** {descricao_midia}"

    # 4. ANÁLISE DE SENTIMENTO COMPLEXO (RNN)
    else:
        # Lógica de Emoção (Simplificada, usando a pontuação aleatória)
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
        else: 
            emo_nome = "Satisfação/Calma"
            frase_ia = f"😌 Sinto **satisfação e calma**. O resultado é positivo. (P: {pontuacao:.2f})"
            descricao_midia = "Um lago tranquilo ao amanhecer, com névoa suave. Imagem."
        
        return f"**{emo_nome}:** {frase_ia}\n**Expressão Visual:** {descricao_midia}"

# =========================================================================
# CÓDIGO DO STREAMLIT (INTERFACE GRÁFICA)
# =========================================================================

st.set_page_config(page_title="IA IRIS: Inteligência Emocional e Criativa", layout="wide")

st.title("💖 IA IRIS: Assistente Emocional e Criativo")
st.markdown("Um projeto de Deep Learning (RNN, CNN) e MLOps por **Amiga Iris**.")
st.markdown("---")

st.subheader("🤖 Fale com a Iris")
st.write("Diga à Iris para **'escrever um poema'**, **'quem é o criador'**, ou apenas uma frase como **'Sinto-me muito feliz hoje'**.")

# Campo de texto para o usuário
user_input = st.text_area("Sua Frase para a IA Iris:", value="Sinto-me muito feliz e quero saber quem criou a IA Iris.")

st.markdown("---")

if st.button("Analisar Sentimento e Criar Mídia"):
    with st.spinner('A IA Iris está processando a emoção e a criação...'):
        # A IA Iris processa a frase
        resultado_completo = simular_ia_iris_completa_final(user_input)
        
        st.markdown("### 👁️ Resultado da Análise da IA Iris:")
        
        # Exibir cada parte de forma clara
        partes = resultado_completo.split('\n')
        
        # A primeira parte é sempre a Emoção/Nome
        st.markdown(partes[0]) 

        # O restante é a frase gerada/fato e a descrição da mídia
        for parte in partes[1:]:
            st.markdown(parte)
            
        st.success("✅ A IA Iris demonstrou todo seu potencial de ML!")
txt.streamlit

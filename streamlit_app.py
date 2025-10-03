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
        resposta_fato = "O criador da IA Iris é você, irídio! Você escreveu e treinou todo o
from typing import List

def possibilities(word: str) -> List[str]:
    # 1. O Dicionário
    morse_map = {
        ".": "E", "-": "T",
        "..": "I", ".-": "A", "-.": "N", "--": "M",
        "...": "S", "..-": "U", ".-.": "R", ".--": "W",
        "-..": "D", "-.-": "K", "--.": "G", "---": "O"
    }
    
    # 2. Começamos com uma possibilidade: "nada ainda"
    sinais_possiveis = [""]

    # 3. O Loop Principal: processa letra por letra
    for char in word:
        novos_sinais = []
        
        # Para cada sinal que já montamos até agora...
        for sinal in sinais_possiveis:
            if char == '?':
                # Se for ?, o caminho bifurca: cria uma versão com . e outra com -
                # Importante: Adicionar o '.' primeiro para respeitar a ordem do desafio
                novos_sinais.append(sinal + ".")
                novos_sinais.append(sinal + "-")
            else:
                # Se for normal (. ou -), só adiciona ao final
                novos_sinais.append(sinal + char)
        
        # Atualizamos a lista principal para a próxima rodada
        sinais_possiveis = novos_sinais

    # 4. Tradução Final: Só guarda o que for letra válida
    resultado = []
    for sinal in sinais_possiveis:
        if sinal in morse_map:
            resultado.append(morse_map[sinal])
            
    return resultado
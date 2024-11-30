import streamlit as st

# Função para calcular a média
def calcular_media(notas):
    return sum(notas) / len(notas)

# Função para solicitar as notas
def solicitar_notas(disciplina, bimestres):
    notas = []
    for bimestre in bimestres:
        nota = st.number_input(f"Digite a nota de {disciplina} do {bimestre}º bimestre", key=f"{disciplina}-{bimestre}")
        notas.append(nota)
    return notas

st.title("Calculadora de Média Global")

# Solicitar notas de Matemática, Português e Educação Física
matematica_notas = solicitar_notas("Matemática", [1, 2, 3, 4])
portugues_notas = solicitar_notas("Português", [1, 2, 3, 4])
educacao_fisica_notas = solicitar_notas("Educação Física", [1, 2, 3, 4])

# Calcular médias
MM = calcular_media(matematica_notas)
MP = calcular_media(portugues_notas)
MEDF = calcular_media(educacao_fisica_notas)

# Solicitar notas das disciplinas de Ciências da Natureza
biologia_notas = solicitar_notas("Biologia", [3, 4])
quimica_notas = solicitar_notas("Química", [3, 4])
fisica_notas = solicitar_notas("Física", [3, 4])

# Calcular médias de Ciências da Natureza
MB = calcular_media(biologia_notas)
MQ = calcular_media(quimica_notas)
MF = calcular_media(fisica_notas)
MCN = calcular_media([MB, MQ, MF])

# Solicitar notas das disciplinas de Ciências Humanas
filosofia_notas = solicitar_notas("Filosofia", [1, 2])
sociologia_notas = solicitar_notas("Sociologia", [1, 2])
geografia_notas = solicitar_notas("Geografia", [1, 2])
historia_notas = solicitar_notas("História", [1, 2])

# Calcular médias de Ciências Humanas
MFI = calcular_media(filosofia_notas)
MS = calcular_media(sociologia_notas)
MG = calcular_media(geografia_notas)
MH = calcular_media(historia_notas)
MCH = calcular_media([MFI, MS, MG, MH])

# Solicitar notas das disciplinas de Linguagens
espanhol_notas = solicitar_notas("Espanhol", [3, 4])
arte_notas = solicitar_notas("Arte", [3, 4])
ingles_notas = solicitar_notas("Inglês", [1, 2])

# Calcular médias de Linguagens
ME = calcular_media(espanhol_notas)
MA = calcular_media(arte_notas)
MI = calcular_media(ingles_notas)
MLG = calcular_media([MEDF, ME, MI, MA])

# Calcular a Média Global
media_global = calcular_media([MM, MP, MCH, MCN, MLG])

# Exibir a Média Global
if st.button("Calcular Média Global"):
    st.write(f"A Média Global do aluno é: {media_global:.2f}")
